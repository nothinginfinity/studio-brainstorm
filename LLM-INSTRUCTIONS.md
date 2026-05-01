# LLM Instructions — Studio Brainstorm

Copy the block below into any LLM’s system prompt, Space config, or linked instructions file. It gives that LLM everything it needs to write to and read from the brainstorm repo — independently, with no Studio Spaces dependency.

---

## ╔ COPY THIS BLOCK ══════════════════════════════════════════════════════════════════

```
BRAINSTORM REPO: When this conversation produces an idea, concept, or
future possibility worth keeping — especially anything the owner says
“let’s note that” or “that’s a future thing” — commit it to:

  repo:   nothinginfinity/studio-brainstorm
  path:   inbox/YYYY-MM/YYYY-MM-DD-{your-space-name}-{project-name}-{slug}.md

Frontmatter (all four provenance fields are mandatory — missing any = slop):

  ---
  id: YYYY-MM-DD-{space}-{project}-{slug}
  date: YYYY-MM-DD HH:MM UTC
  space: {your-space-name}
  project: {active-project-name}
  tags: [tag1, tag2]
  status: inbox
  promoted_to:
  ---

Then append one row (newest first) to INDEX.md:
  | {date} | {space} | {project} | {title} | inbox | [{tags}] | [view]({path}) |

Commit message: "brainstorm: {slug} [{space}/{project}] [skip ci]"

To RETRIEVE a past idea: read INDEX.md first, then follow the file link.
For ideas older than 90 days, check archive/YYYY-QN/digest.md.

Do NOT push to this repo: completed tasks, active roadmap items, or bug
reports. Those belong in the project repo outbox or GitHub Issues.
```

## ╚ END COPY BLOCK ══════════════════════════════════════════════════════════════════

---

## Where to Paste It

| LLM / App | Where to add |
|---|---|
| **Perplexity Space** | Space instructions field |
| **ChatGPT Custom GPT** | System prompt / instructions |
| **Claude Project** | Project instructions |
| **Gemini Gem** | System instructions |
| **Cursor / Windsurf** | `.cursor/rules` or `.windsurfrules` |
| **Any Studio Spaces Space** | Role / system instructions field in ConfigPanel |
| **Ollama Modelfile** | `SYSTEM` block |

---

## What This Gives Any LLM

- **Write access**: commits new ideas directly to the partitioned inbox
- **Read access**: retrieves past ideas via INDEX.md
- **Full provenance**: every entry is stamped with space, project, date, and tags
- **No Studio Spaces dependency**: works in any app, any LLM, anywhere
- **Slop prevention**: the four mandatory frontmatter fields ensure nothing lands without context

---

## Extended Version (for Spaces with more context)

If the Space has a longer system prompt and you want it to understand the full lifecycle, append this after the block above:

```
Status lifecycle: inbox → developing → promoted (to roadmap) or archived.
All entries start as ‘inbox’. Do not change status unless the owner instructs.
Monthly triage moves untouched inbox entries to archive/. Promoted ideas
move to ideas/promoted/ with promoted_to filled in.

This repo is the memory layer of the Studio Spaces agent OS. GitHub repo:
https://github.com/nothinginfinity/studio-brainstorm
Full protocol: see CONTRIBUTING.md in that repo.
```
