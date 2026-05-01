---
id: 2026-04-30-local-gitea-forgejo
date: 2026-04-30 21:45 UTC
space: bob
project: studio-spaces
tags: [gitea, forgejo, local-first, offline, provider-abstraction, self-hosted]
status: promoted
promoted_to: ROADMAPspaces.md (Phase 4 + Local-First Target section)
---

## Local-First Studio Spaces via Gitea / Forgejo

### The Concept

GitHub goes down. Or you want faster local operation. Or you want air-gapped privacy. Studio Spaces should be able to run the entire agent OS workflow against a self-hosted git forge (Gitea or Forgejo) instead of GitHub — with zero changes to the MMCP protocol or agent behavior.

### Why It Matters

- Speed: local git operations are orders of magnitude faster than GitHub API calls
- Resilience: not dependent on GitHub uptime
- Privacy: sensitive projects stay on your own hardware
- Portability: the same workflow, the same agents, the same MMCP protocol — just a different remote

### How It Might Work

- Provider abstraction layer in `src/providers/git-provider.js`
- Config setting: `provider: "github" | "gitea" | "forgejo"`
- Custom `baseUrl` per project pointing at local Gitea instance
- Gitea Actions uses same YAML syntax as GitHub Actions — zero CI changes
- Ollama handles local model execution for fully air-gapped operation

### Strategy

Build GitHub-first, but never GitHub-only. Introduce the abstraction in Phase 4 before hard dependencies accumulate. Gitea/Forgejo support is a few hours of work at that point, not a rewrite.

### Open Questions

- Gitea Actions runner: does it need to be self-hosted or can it use a cloud runner?
- Web Push relay in local mode: run a local Express server instead of Cloudflare Worker?

### Related Ideas

- [repo-native-agent-os](2026-04-30-repo-native-agent-os.md)
