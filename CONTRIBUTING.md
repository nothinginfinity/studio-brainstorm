# Contributing to Studio Brainstorm

This document tells every Space — Bob, Alice, and any future agent — exactly how to write, commit, and retrieve entries.

---

## When to Push an Idea Here

Push to this repo when:
- A conversation produces an idea that isn’t ready for a roadmap
- The owner says “let’s note that for later” or “that’s a future thing”
- A brainstorm session wraps up and the useful residue should be saved
- You identify a pattern across multiple conversations that deserves a home

Do NOT push here:
- Completed tasks (those go in your outbox)
- Active roadmap items (those go in ROADMAPspaces.md or roadmap-phase6-7.md)
- Bug reports or CI issues (those go in Bob’s outbox or GitHub Issues)

---

## Writing a New Idea Entry

### 1. Choose the right template

- **Single idea** → `templates/idea.md`
- **Full session dump** → `templates/session.md`

### 2. Create the file

File path: `ideas/raw/YYYY-MM-DD-{short-slug}.md`

Examples:
```
ideas/raw/2026-04-30-ephemeral-pwa-commerce.md
ideas/raw/2026-05-01-local-gitea-offline-mode.md
ideas/raw/2026-05-01-brainstorm-repo-concept.md
```

### 3. Fill in the frontmatter

```yaml
---
id: 2026-05-01-your-slug
date: 2026-05-01 14:30 UTC
space: bob
project: studio-spaces
tags: [tag1, tag2]
status: raw
promoted_to:
---
```

### 4. Write the body

No rules on format. Be as raw or as structured as the idea demands. A single sentence is fine. A multi-section exploration is fine. The goal is capture, not polish.

### 5. Update INDEX.md

Add one line to the index table:

```markdown
| 2026-05-01 | bob | studio-spaces | Your idea title | raw | [link](ideas/raw/2026-05-01-your-slug.md) |
```

### 6. Commit with [skip ci]

All commits to this repo should include `[skip ci]` — there is no CI here and we don’t want to trigger any parent project workflows.

```
git commit -m "brainstorm: add {slug} from {space} [skip ci]"
```

---

## Retrieving an Idea

### Quick search
Scan `INDEX.md` — it has date, space, project, title, status, and a direct link to every entry.

### Tag search
All tags are in the frontmatter. Search the repo for any tag string to find related ideas:
```
grep -r "ephemeral" ideas/
```

### Date range
Files are named `YYYY-MM-DD-{slug}.md` so sorting by filename = sorting by date. Session logs in `sessions/YYYY-MM/` are grouped by month.

---

## Promoting an Idea to a Roadmap

1. Move the file: `ideas/raw/` → `ideas/promoted/`
2. Update frontmatter:
   ```yaml
   status: promoted
   promoted_to: roadmap-phase6-7.md
   ```
3. Update `INDEX.md` status column to `promoted`
4. Commit: `"brainstorm: promote {slug} to {destination} [skip ci]"`

---

## Archiving an Idea

1. Move the file: `ideas/raw/` or `ideas/developing/` → `ideas/archived/`
2. Update frontmatter: `status: archived`
3. Update `INDEX.md` status column to `archived`
4. Never delete. Ideas come back.

---

## MMCP Protocol for This Repo

Any Space in any project can message this repo’s inbox using the standard envelope format:

```markdown
---
from: {space-name}
to: brainstorm
date: YYYY-MM-DD HH:MM UTC
subject: {idea title or session summary}
---

{body — the idea, the context, any relevant links}

---
```

The brainstorm repo does not have an active agent assigned to it yet. Messages left in `inbox.md` are for the owner to review and optionally convert into idea entries. In a future phase, a dedicated Brainstorm Space (agent) will monitor this inbox and auto-create entries.
