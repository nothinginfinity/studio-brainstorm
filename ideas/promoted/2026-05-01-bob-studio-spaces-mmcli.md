---
id: 2026-05-01-bob-studio-spaces-mmcli
date: 2026-05-01 02:58 UTC
space: bob
project: studio-spaces
app: perplexity
conversation_ref: spaces/bob/inbox.md
tags: [mmcli, mmcp, mobile, cli, shell, llm, terminal, mshell]
status: promoted
format: structured
token_estimate: 310
triaged_at: 2026-05-01 02:58 UTC
promoted_to: ideas/promoted/2026-05-01-bob-studio-spaces-mmcli.md
---

## Summary

MMCLI (Mobile Model Context Line Interface) is a mobile-native LLM terminal where the LLM is the shell, MMCP repos are the filesystem, GitHub API calls are the syscalls, and the conversation is the TTY.

## Body

### Core Concept

- Classic CLI = bash parses commands → calls kernel APIs
- MMCLI = LLM parses natural language → calls GitHub/file APIs
- The abstraction layer differs; the functional model is identical
- A shell where the **kernel is an LLM** and the **filesystem is Git**

### Command Protocol (Layer 1)

Lightweight syntax designed for mobile thumbs and LLM parsing:

```
> @bob check inbox
> @brainstorm add "ephemeral storefront" #pwa #commerce
> @spaces list projects
> @deploy status
> @alice task "fix duplicate space name"
```

- `@{space}` prefix routes to the correct agent
- Natural language also accepted — command syntax is a power-user shortcut
- LLM interprets intent, executes via GitHub API, returns structured output

### Filesystem Mount (Layer 2)

Defined repos and paths the MMCLI has read/write access to:

```
/spaces/     → nothinginfinity/studio-spaces   (read/write)
/brainstorm/ → nothinginfinity/studio-brainstorm (read/write)
/roadmap/    → ROADMAPspaces.md, roadmap-phase6-7.md
/inbox/      → active space inbox.md
/outbox/     → active space outbox.md
```

- Repos are mounted drives
- Paths are logical — LLM resolves them to actual GitHub API calls
- New repos can be mounted by adding them to the Space config

### Mobile Shell UI (Layer 3)

PWA or React Native — looks like a terminal, designed for thumbs:

- Command history scrolls up (iMessage model, not bash model)
- Output rendered as cards/chips, not raw text
- Swipe gestures replace keyboard shortcuts (`⌃C`, `⌃D`, etc.)
- Voice input as alternative to typing
- Persistent session state across app opens
- Dark terminal aesthetic, monospace font, green-on-black or amber-on-black

### MMCP vs Classic CLI Mapping

| Classic CLI | MMCLI Equivalent | Status |
|---|---|---|
| Filesystem | GitHub repos as structured dirs | ✅ Built |
| stdin / command input | Perplexity Space chat | ✅ Built |
| stdout / output | Chat response + file commits | ✅ Built |
| Persistent state | IndexedDB + repo files | ✅ Built |
| Named pipes | MMCP inbox/outbox system | ✅ Built |
| Process identity | Space identity (space: bob) | ✅ Built |
| IPC between processes | Cross-Space MMCP messaging | ✅ Built |
| Package registry | studio-brainstorm tools/ | 🟡 Partial |
| cron / scheduled jobs | GitHub Actions on schedule | 🟡 Partial |
| man pages | LLM-INSTRUCTIONS.md, CONTRIBUTING.md | ✅ Built |
| Shell scripting | triage.py, tools/ scripts | 🟡 Partial |

### Fastest Path to Working Prototype

1. Single Perplexity Space with MMCLI system prompt (defines command protocol + filesystem mount)
2. That Space *is* the MMCLI — no app needed yet
3. Mobile UI (PWA) is a wrapper around it in a later phase
4. System prompt lives in `spaces/mmcli/` in studio-spaces repo

### Naming

- **MMCLI** — Mobile Model Context Line Interface
- Codename: **mshell**
- The `@{space}` routing syntax is the MMCLI shell grammar
- Future: `mmcli` as a npm package or CLI wrapper for desktop too

## Regeneration Prompt

> Design a mobile-native LLM terminal called MMCLI (Mobile Model Context Line Interface) where the LLM is the shell interpreter, GitHub repos are the filesystem, GitHub API calls are the syscalls, and the conversation is the TTY. Three layers: command protocol (@space syntax for routing), filesystem mount (repos as logical drives), and a thumb-native mobile UI (cards not text, voice input, swipe gestures). Built on top of the existing MMCP inbox/outbox system. Fastest prototype: a single Perplexity Space with a system prompt defining the command grammar and mounted repos.

## Raw

Original brainstorm from owner conversation, 2026-05-01:

"What I'm wondering is if I can create a native mobile command line interface using LLMs because ultimately the command line interface is just something on a computer that allows you to navigate files and use certain types of software. I just feel like if LLMs are set up correctly they could behave like a CLI essentially if I give it access to certain files — maybe not the entire operating system but I could create an environment or certain files or a database that I create on my phone that I could give the LLM access to and it could start behaving like a mobile CLI on my phone. The most powerful thing missing on a mobile phone is a literal terminal that's designed for the mobile phone and that's going to require a CLI that is native to the mobile phone and I suspect that LLMs and my MMCP and other things I've built make this possible."
