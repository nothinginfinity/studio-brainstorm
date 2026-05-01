# Studio Brainstorm

> The cross-project idea memory for the Studio Spaces agent OS.

This repository is the **recycling center** of every Studio Spaces conversation. Not a codebase. Not a product. A place where raw thinking, half-baked ideas, and future concepts are captured, indexed, and made permanently retrievable by any agent in any project.

---

## The Rule

**If an idea is good enough to say out loud, it's good enough to commit here.**

Every Space in every Studio Spaces project should have read/write access to this repo. When a conversation produces a brainstorm that isn't ready for a roadmap, it gets pushed here instead of disappearing into chat history.

---

## Structure

```
studio-brainstorm/
├── README.md                  ← this file
├── CONTRIBUTING.md            ← how to write and push brainstorm entries
├── INDEX.md                   ← master searchable index of all entries
├── inbox.md                   ← MMCP inbox — other Spaces message here
├── templates/
│   ├── idea.md                ← standard idea entry template
│   └── session.md             ← full conversation brainstorm session template
├── ideas/
│   ├── raw/                   ← unfiltered, just captured
│   ├── developing/            ← being fleshed out, has potential
│   ├── promoted/              ← graduated to a real roadmap or project
│   └── archived/              ← evaluated, set aside — not deleted, just parked
└── sessions/                  ← full brainstorm session logs by date
    └── YYYY-MM/               ← grouped by month
```

---

## Status Lifecycle

```
raw → developing → promoted (moves to roadmap)
              └→ archived  (evaluated, parked)
```

- **raw** — just captured, unfiltered. Default for all new entries.
- **developing** — revisited, has legs, being fleshed out.
- **promoted** — graduated to a real roadmap file or project. Note the destination in `promoted_to`.
- **archived** — evaluated and intentionally set aside. Never deleted — ideas come back.

---

## How Agents Use This Repo

**Writing (capturing an idea):**
1. Use the template in `templates/idea.md`
2. Fill in the frontmatter metadata
3. Commit to `ideas/raw/{date}-{slug}.md`
4. Update `INDEX.md` with a one-line entry

**Reading (finding a past idea):**
1. Search `INDEX.md` by tag, project, space, or date range
2. Follow the file path to the full entry
3. Reference the idea in the current conversation

**Promoting (idea graduated to roadmap):**
1. Move the file from `ideas/raw/` to `ideas/promoted/`
2. Update frontmatter: `status: promoted`, `promoted_to: {roadmap file}`
3. Update `INDEX.md` status column

---

## Metadata Reference

Every entry begins with a YAML frontmatter block:

```yaml
---
id: {YYYY-MM-DD}-{short-slug}
date: YYYY-MM-DD HH:MM UTC
space: {space-name}          # which agent/space originated this
project: {project-name}      # which project the conversation was in
tags: [tag1, tag2, tag3]     # freeform, lowercase, hyphenated
status: raw                  # raw | developing | promoted | archived
promoted_to:                 # leave blank unless promoted
---
```

---

*This repo has no issues, no PRs, no CI. It is a knowledge base. Treat every commit as a message to your future self.*
