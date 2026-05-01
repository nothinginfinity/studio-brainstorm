# Contributing to Studio Brainstorm

This is the full protocol for any agent — Bob, Alice, or any LLM in any app — to write, retrieve, and triage entries. For the one-paragraph version to paste into a system prompt, see `LLM-INSTRUCTIONS.md`.

---

## This Repo is Independent

Studio Brainstorm does **not** depend on Studio Spaces being installed or running. Any LLM with:
- A GitHub personal access token (with `repo` scope)
- Knowledge of this entry format

...can write here directly via the GitHub API. No SDK. No server. No Studio Spaces.

---

## Dual-Write Pattern

Every agent should write to TWO places per session:

```
1. Project repo outbox     → what was BUILT or DONE
   spaces/{name}/outbox.md in the project repo

2. studio-brainstorm       → what was THOUGHT or IMAGINED
   inbox/YYYY-MM/{date}-{space}-{project}-{slug}.md
```

These are different concerns and should never be merged.

---

## Writing a New Inbox Entry

### Step 1 — Filename

All new entries go into `inbox/YYYY-MM/` partitioned by the current month:

```
inbox/2026-05/2026-05-01-bob-studio-spaces-ephemeral-pwa.md
```

Filename format: `YYYY-MM-DD-{space}-{project}-{slug}.md`
- `space` — your space/agent name (lowercase, no spaces)
- `project` — the project this idea came from (lowercase, hyphenated)
- `slug` — 2-5 word description (lowercase, hyphenated)

The filename itself encodes full provenance. No database needed.

### Step 2 — Frontmatter (required, no exceptions)

```yaml
---
id: 2026-05-01-bob-studio-spaces-ephemeral-pwa
date: 2026-05-01 14:30 UTC
space: bob
project: studio-spaces
app: perplexity               # optional
conversation_ref:             # optional: URL or ID
tags: [ephemeral, commerce, pwa]
status: inbox
promoted_to:
---
```

Missing frontmatter = slop. All four provenance fields (`id`, `date`, `space`, `project`) are mandatory.

### Step 3 — Body

No format rules. A single sentence is fine. A multi-section write-up is fine. The goal is capture, not polish.

### Step 4 — Update INDEX.md

Append one row at the TOP of the index table (newest first):

```
| 2026-05-01 | bob | studio-spaces | Your Idea Title | inbox | [ephemeral, commerce] | [view](inbox/2026-05/2026-05-01-bob-studio-spaces-your-slug.md) |
```

### Step 5 — Commit

```
brainstorm: {slug} [{space}/{project}] [skip ci]
```

Always include `[skip ci]`. This repo has no CI and we don't want to trigger parent project workflows.

---

## Retrieving a Past Idea

### Option 1: INDEX.md (fastest)
Search `INDEX.md` — one row per idea, newest first. Columns: date, space, project, title, status, tags, link.

### Option 2: Filename search
All files are named `YYYY-MM-DD-{space}-{project}-{slug}.md`. Sort by name = sort by date. Filter by `{project}` to find all ideas from a specific project.

### Option 3: Tag search
```
grep -r "tag-name" inbox/ ideas/
```

### Option 4: Archive
For ideas older than ~90 days, check `archive/YYYY-QN/digest.md`. For ideas older than ~1 year, check `archive/YYYY/annual.md`.

---

## Triage Protocol

### Weekly (light)
- Scan `inbox/YYYY-MM/` for entries from the past 7 days
- Move anything with clear legs to `ideas/developing/`
- Update `INDEX.md` status column
- Leave everything else in inbox

### Monthly
- Any inbox entry older than 30 days that hasn’t moved to `developing` → move to `archive/YYYY-QN/`
- Update `INDEX.md`

### Quarterly
- Compress all monthly folders in `archive/YYYY-QN/` into a single `digest.md` summary
- Delete the individual monthly files (the digest is the record)
- Update `INDEX.md` archive entries to point to digest

### Annual
- Merge all quarter digests into `archive/YYYY/annual.md`
- Delete individual quarter digests
- This keeps the repo lean regardless of volume

---

## Promoting to a Roadmap

1. Move file: `inbox/YYYY-MM/` or `ideas/developing/` → `ideas/promoted/`
2. Update frontmatter: `status: promoted`, `promoted_to: {destination file}`
3. Update `INDEX.md` row
4. Commit: `brainstorm: promote {slug} to {destination} [skip ci]`

---

## Archiving an Idea

1. Move file to `ideas/archived/`
2. Update frontmatter: `status: archived`
3. Update `INDEX.md`
4. Never delete. Ideas come back.

---

## MMCP Envelope for This Repo

Any Space can drop a message into this repo’s inbox using the standard MMCP envelope, committed directly to `inbox/YYYY-MM/` with a properly named file:

```markdown
---
from: alice
to: brainstorm
date: 2026-05-01 15:00 UTC
subject: Sidebar animation idea
---

Body of the idea...

---
```

The filename still follows the provenance convention: `2026-05-01-alice-studio-spaces-sidebar-animation.md`
