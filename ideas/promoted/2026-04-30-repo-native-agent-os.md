---
id: 2026-04-30-repo-native-agent-os
date: 2026-04-30 21:30 UTC
space: bob
project: studio-spaces
tags: [agent-os, mcp, repo-primitives, architecture, github, git, mobile-first]
status: promoted
promoted_to: ROADMAPspaces.md (The Bigger Picture section)
---

## Repo-Native Agent OS — GitHub as the Hard Drive

### The Concept

Studio Spaces is not just a chat app. It is a repo-native, mobile-first agent operating system where GitHub repositories serve every role a traditional OS filesystem would serve — but with version control, auditability, and multi-agent access built in by default.

### Why It Matters

Traditional MCP requires a running server, API endpoints, and a client SDK. This architecture achieves the same result using only git. No daemon. No server. No SDK. Works from a phone. Every tool call, message, and result is a git commit — nothing is ever lost.

### Repo Type Taxonomy

- **Codebase repo** — executable / application
- **Skill repo** — `.md` files = shared knowledge library
- **Tool repo** — runnable code = system utility
- **Template repo** — scaffold for new projects
- **Memory repo** — commit history = persistent agent memory
- **MMCP bus** — `spaces/*/inbox.md` = inter-agent message queue

### Open Questions

- How does this scale to 100+ repos? Does the agent OS need a registry?
- Can a skill repo be auto-discovered or does it need to be explicitly linked?

### Related Ideas

- [local-gitea-forgejo](2026-04-30-local-gitea-forgejo.md)
- [studio-brainstorm-repo](../2026-05-01-studio-brainstorm-repo.md)
