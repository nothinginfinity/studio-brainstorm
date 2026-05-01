#!/usr/bin/env python3
"""
studio-brainstorm/tools/triage.py

The recycling sorter. Reads all `prose` entries in inbox/YYYY-MM/,
classifies each one by the best storage format, converts the body,
generates a compressed regeneration prompt, updates frontmatter,
and writes the result back in the three-layer structure.

Requires:
  pip install openai python-frontmatter tiktoken

Usage:
  python tools/triage.py                       # dry run, prints plan only
  python tools/triage.py --write               # writes changes to disk
  python tools/triage.py --month 2026-05       # target a specific month
  python tools/triage.py --file inbox/2026-05/x.md  # single file

Environment:
  OPENAI_API_KEY        required
  BRAINSTORM_MODEL      optional, default: gpt-4o-mini
"""

import os
import sys
import argparse
import textwrap
from pathlib import Path
from datetime import datetime, timezone

try:
    import frontmatter
    import tiktoken
except ImportError:
    print("Missing deps. Run: pip install python-frontmatter tiktoken openai")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT  = Path(__file__).parent.parent
INBOX_ROOT = REPO_ROOT / "inbox"
MODEL      = os.environ.get("BRAINSTORM_MODEL", "gpt-4o-mini")

FORMAT_DESCRIPTIONS = {
    "structured": "Bulleted markdown. Best for product/feature/UX ideas.",
    "python":     "Runnable sketch. Best for technical/algorithmic ideas.",
    "mermaid":    "Diagram in mermaid fences. Best for architecture/flow ideas.",
    "prompt":     "Compressed 40-80 word seed. Best for conceptual ideas.",
}

CLASSIFY_SYSTEM = """
You are a brainstorm archivist. Given a raw idea dump, choose the best
storage format to minimize tokens while preserving full reconstructability.

Formats:
- structured  : product/feature/UX idea with clear named components
- python      : technical/algorithmic idea expressible as a class or function sketch
- mermaid     : architecture, flow, or relationship idea
- prompt      : conceptual/philosophical idea best stored as a dense regen seed

Respond with ONLY one word: structured | python | mermaid | prompt
"""

CONVERT_SYSTEM = """
Convert the raw idea dump into the specified compact format.
Preserve all meaning. Minimize tokens. No preamble, no explanation.

Rules per format:
- structured : ## subheadings + bullets only. No prose paragraphs.
- python     : class or function sketch under 30 lines. Key-concept comments only.
- mermaid    : valid Mermaid diagram in ```mermaid fences. Nodes = key concepts.
- prompt     : ONE paragraph, 40-80 words. Dense enough to reconstruct the idea.
"""

REGEN_SYSTEM = """
Write a single compressed regeneration prompt (40-80 words) for the idea below.
An LLM reading only this prompt must be able to reconstruct the full original idea
with high fidelity. Return ONLY the prompt text. No preamble.
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def count_tokens(text: str) -> int:
    try:
        enc = tiktoken.encoding_for_model(MODEL)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def llm(system: str, user: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set.")
    try:
        from openai import OpenAI
    except ImportError:
        print("Run: pip install openai")
        sys.exit(1)
    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
        temperature=0.2,
        max_tokens=1024,
    )
    return resp.choices[0].message.content.strip()


def rebuild_content(summary_block: str, converted_body: str,
                    regen_prompt: str, original_content: str) -> str:
    parts = [
        summary_block.strip(),
        "",
        "## Body",
        "",
        converted_body.strip(),
        "",
        "## Regeneration Prompt",
        "",
        f"> {regen_prompt.strip()}",
        "",
        "## Raw",
        "",
        "<!-- Original prose preserved below. Do not edit. -->",
        "",
        original_content.strip(),
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Core triage
# ---------------------------------------------------------------------------

def triage_file(path: Path, write: bool = False) -> dict:
    post = frontmatter.load(str(path))
    meta    = post.metadata
    content = post.content

    if meta.get("format", "prose") != "prose":
        return {"file": str(path), "skipped": True,
                "reason": f"format={meta.get('format')}"}

    print(f"\n{'='*60}")
    print(f"File   : {path.name}")
    print(f"Tags   : {meta.get('tags', [])}")
    print(f"Project: {meta.get('project', '?')} / Space: {meta.get('space', '?')}")

    # Isolate summary vs body
    summary_block = ""
    raw_body = content
    if "## Body" in content:
        parts = content.split("## Body", 1)
        summary_block = parts[0]
        raw_body = parts[1].split("## ")[0].strip()  # stop at next section

    token_before = count_tokens(raw_body)

    # 1. Classify
    target_format = llm(CLASSIFY_SYSTEM, raw_body).lower().strip()
    if target_format not in FORMAT_DESCRIPTIONS:
        target_format = "structured"
    print(f"  → Format   : {target_format}  ({FORMAT_DESCRIPTIONS[target_format]})")

    # 2. Convert
    converted = llm(CONVERT_SYSTEM, f"Format: {target_format}\n\nOriginal:\n{raw_body}")
    token_after = count_tokens(converted)
    saved_pct   = round((1 - token_after / max(token_before, 1)) * 100)
    print(f"  → Tokens   : {token_before} → {token_after} ({saved_pct}% reduction)")

    # 3. Regen prompt
    regen = llm(REGEN_SYSTEM, raw_body)
    print(f"  → Regen    : {regen[:80]}...")

    report = {
        "file": str(path),
        "skipped": False,
        "new_format": target_format,
        "token_before": token_before,
        "token_after": token_after,
        "converted": converted,
        "regen": regen,
    }

    if write:
        meta["format"]        = target_format
        meta["token_estimate"] = token_after
        meta["triaged_at"]    = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

        new_content = rebuild_content(
            summary_block if summary_block else "## Summary\n\n(see raw)\n",
            converted,
            regen,
            content,
        )
        post.content  = new_content
        post.metadata = meta

        with open(path, "w", encoding="utf-8") as f:
            f.write(frontmatter.dumps(post))
        print("  ✓ Written.")

    return report


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Studio Brainstorm triage sorter")
    parser.add_argument("--write",  action="store_true",
                        help="Write changes to disk (default: dry run)")
    parser.add_argument("--month",  type=str,
                        help="Target month, e.g. 2026-05")
    parser.add_argument("--file",   type=str,
                        help="Triage a single file path")
    args = parser.parse_args()

    if args.file:
        files = [Path(args.file)]
    elif args.month:
        files = sorted((INBOX_ROOT / args.month).glob("*.md"))
    else:
        files = sorted(INBOX_ROOT.glob("**/*.md"))
        files = [f for f in files if f.name != ".gitkeep"]

    if not files:
        print("No files found.")
        return

    mode = "WRITE" if args.write else "DRY RUN"
    print(f"{mode} — {len(files)} file(s) to inspect")

    reports  = [triage_file(f, write=args.write) for f in files]
    done     = [r for r in reports if not r.get("skipped")]
    skipped  = [r for r in reports if r.get("skipped")]
    saved    = sum(r["token_before"] - r["token_after"] for r in done)

    print(f"\n{'='*60}")
    print(f"Triage complete.")
    print(f"  Processed    : {len(done)}")
    print(f"  Skipped      : {len(skipped)} (already triaged)")
    print(f"  Tokens saved : ~{saved}")
    if not args.write:
        print("\n  DRY RUN — re-run with --write to apply.")


if __name__ == "__main__":
    main()
