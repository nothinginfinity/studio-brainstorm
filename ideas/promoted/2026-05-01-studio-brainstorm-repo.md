---
id: 2026-05-01-studio-brainstorm-repo
date: 2026-05-01 14:26 UTC
space: bob
project: studio-spaces
tags: [brainstorm, memory, mmcp, agent-os, knowledge-base, cross-project]
status: promoted
promoted_to: this repo (studio-brainstorm) — the idea became the artifact
---

## Studio Brainstorm Repo — Cross-Project Idea Memory

### The Concept

A dedicated GitHub repo that every Space in every project can write to and read from. Raw brainstorms, half-baked ideas, and future concepts are committed here with structured metadata instead of disappearing into chat history. The repo is a searchable, agent-readable knowledge base — the recycling center of all Studio Spaces conversations.

### Why It Matters

Conversations are 20% work, 80% brainstorm. The 80% is valuable but perishable. Without a capture system, every good idea that doesn’t make a roadmap is lost. This repo is the fix: a permanent, indexed home for the residue of every conversation, accessible by any future agent in any future project.

### How It Works

- Every entry has YAML frontmatter: `id`, `date`, `space`, `project`, `tags`, `status`, `promoted_to`
- `status` lifecycle: `raw → developing → promoted` or `→ archived`
- `INDEX.md` is the master search surface — one row per idea, newest first
- Any Space pushes here via standard MMCP commit or directly via the GitHub API
- Any agent searching for a past idea reads `INDEX.md` first, then follows the file link

### The Retrieval Promise

In three months, any Space can be asked: *“I had an idea about ephemeral storefronts a few weeks ago — find it.”* The agent reads `INDEX.md`, finds the entry by tag or date, returns the full idea with context. Nothing is lost.

### Related Ideas

- [repo-native-agent-os](2026-04-30-repo-native-agent-os.md)
