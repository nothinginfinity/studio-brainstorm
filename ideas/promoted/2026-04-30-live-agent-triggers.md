---
id: 2026-04-30-live-agent-triggers
date: 2026-04-30 21:38 UTC
space: bob
project: studio-spaces
tags: [push-notifications, webhooks, pwa, service-worker, agent-triggers, always-on]
status: promoted
promoted_to: ROADMAPspaces.md (Phase 5)
---

## Live Agent Triggers via Webhook + Web Push

### The Concept

When an agent commits to a Space’s inbox, the owner’s phone receives a native push notification within seconds. Tapping the notification opens the correct Space with the new message visible. One more tap resumes the agent collaboration thread. No polling. No checking. The system is always running.

### Why It Matters

This is the difference between "agents that can collaborate" and "agents that are always running." Currently, agents only move as fast as the owner’s attention. Push triggers close that loop — making the MMCP inbox behave like a real-time message queue without any always-on server process.

### How It Might Work

- GitHub push webhook → Cloudflare Worker → parse diff for `spaces/*/inbox.md` changes → extract MMCP envelope → send Web Push
- PWA service worker subscribes to Web Push (VAPID)
- Notification tap deep-links to correct Project → Space
- Optional auto-resume: app pre-populates chat input with “You have a new message…”
- Works on iOS 16.4+ (Safari PWA) and Android Chrome

### Open Questions

- Cloudflare Worker free tier limits: 100k requests/day — sufficient for personal use?
- iOS Safari PWA push: requires user to add to Home Screen first
- Quiet hours UX: system-level DND or app-level setting?

### Related Ideas

- [repo-native-agent-os](2026-04-30-repo-native-agent-os.md)
- [ephemeral-pwa-commerce](2026-04-30-ephemeral-pwa-commerce.md)
