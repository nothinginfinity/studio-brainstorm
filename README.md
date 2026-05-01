# Studio Brainstorm

> The cross-project idea memory for the Studio Spaces agent OS.
> **Independent of Studio Spaces.** Any LLM, any app, any project can write here with just a GitHub token and the entry format below.

This repository is the **slop management system** for all Studio Spaces conversations — a place where raw thinking, half-baked ideas, and future concepts are captured with full provenance, indexed, and made permanently retrievable by any agent in any project. Unorganized data without metadata is slop. This repo exists to make sure nothing valuable becomes slop.

---

## The Rule

**If an idea is good enough to say out loud, it's good enough to commit here.**

Agents write to TWO places simultaneously:
- **Project repo outbox** — what was *built* (`spaces/{name}/outbox.md` in the project repo)
- **This repo** — what was *thought* (`inbox/YYYY-MM/` here)

These are different concerns. The project outbox is for completed work. This repo is for ideas that aren't ready yet — or may never be, and that's fine.

---

## Structure

```
studio-brainstorm/
├── README.md                        ← this file
├── CONTRIBUTING.md                  ← full protocol for agents
├── LLM-INSTRUCTIONS.md              ← one-paragraph prompt block for any LLM
├── INDEX.md                         ← master searchable index (newest first)
├── inbox/                           ← raw incoming ideas, partitioned by month
│   ├── 2026-05/
│   │   ├── 2026-05-01-bob-studio-spaces-ephemeral-pwa.md
│   │   └── 2026-05-01-alice-studio-spaces-sidebar-idea.md
│   └── YYYY-MM/                     ← one folder per month, auto-created
├── ideas/
│   ├── developing/                  ← promoted from inbox, being fleshed out
│   ├── promoted/                    ← graduated to a real roadmap or project
│   └── archived/                    ← evaluated, set aside — not deleted
├── archive/                         ← compressed historical record
│   ├── 2026-Q2/                     ← quarterly digest of inbox/ideas
│   └── 2026/                        ← annual summary
└── templates/
    ├── idea.md                      ← single idea entry
    └── session.md                   ← full session brainstorm dump
```

**Key change from v1:** Raw ideas now land in `inbox/YYYY-MM/` (not `ideas/raw/`). The inbox is partitioned by month so it never becomes a flat pile. `ideas/` is only for entries that have been triaged — developing, promoted, or archived.

---

## Provenance is Mandatory

Every entry must answer four questions:
1. **Who wrote it?** (`space`)
2. **What project was it from?** (`project`)
3. **When?** (`date` + filename prefix)
4. **What is it about?** (`tags` + title)

An entry without these four fields is slop. The filename itself encodes provenance:
```
inbox/2026-05/2026-05-01-bob-studio-spaces-ephemeral-pwa.md
              └──date──┘ └space┘ └───project──┘ └───slug───┘
```
No database needed to know what the file is.

---

## Status Lifecycle

```
inbox/YYYY-MM/  →  ideas/developing/  →  ideas/promoted/  (roadmap)
                                       └→  ideas/archived/  (parked)
     ↓ (untouched after 30 days)
  archive/YYYY-QN/digest.md
```

- **inbox** — raw, just captured. All new entries start here.
- **developing** — triaged, has potential, being fleshed out.
- **promoted** — graduated to a real roadmap. `promoted_to` field required.
- **archived** — evaluated and intentionally set aside. Never deleted.

---

## Growth Management

| Stage | Trigger | Action |
|---|---|---|
| **Live** | Always | Entries land in `inbox/YYYY-MM/` |
| **Weekly triage** | 7 days | Review inbox; promote to `developing` or leave |
| **Monthly archive** | 30 days | Untouched inbox entries move to `archive/YYYY-QN/` |
| **Quarterly digest** | 90 days | Month folders compressed into `archive/YYYY-QN/digest.md` |
| **Annual summary** | 365 days | Quarter digests merged into `archive/YYYY/annual.md` |

`INDEX.md` always points to the correct location regardless of which stage an entry is in.

---

## Metadata Reference

```yaml
---
id: YYYY-MM-DD-{space}-{project}-{slug}
date: YYYY-MM-DD HH:MM UTC
space: {space-name}          # agent/LLM that originated this
project: {project-name}      # project repo the conversation was about
app: {app-name}              # optional: which app/UI the LLM was running in
conversation_ref:            # optional: link or ID to source conversation
tags: [tag1, tag2, tag3]     # freeform, lowercase, hyphenated
status: inbox                # inbox | developing | promoted | archived
promoted_to:                 # leave blank unless promoted
---
```

---

*This repo has no CI, no issues, no PRs. It is a knowledge base. Every commit is a message to your future self — and to every agent that comes after you.*
