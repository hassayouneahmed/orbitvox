# Security

OrbitVox gives an AI model real powers on your computer: web, links, a browser and your notes. Security reports are very welcome.

## Reporting a problem
Please **don't open a public issue** for a security hole. Use GitHub's **private vulnerability reporting** instead: the Security tab → "Report a vulnerability". Include:
- what you did (steps, or the page or note that triggered it),
- what happened, and what should have happened,
- your OrbitVox version and brain (`claude`, `openrouter` or `openai`).

We aim to reply within 7 days.

## In scope
- Notes leaking into web mode, or the web reaching notes in vault mode.
- Reads outside the notes folder, or of the blocked files (`.env*`, `.git`, `.ssh`, `.claude`, `.obsidian`).
- A web page or note that makes the assistant open a link, switch modes, or use a tool it shouldn't.
- Links that bypass the URL rules (IPs, local hosts, ports, downloads).
- Any way the Claude CLI could use an API key or someone else's login.

## Known limits (accepted for now)
- Its own browser can be steered to local addresses by a web page. It can only browse and click there, with a throwaway profile, and you see the window.
- Audio from other apps can reach the mic; use the M key or headphones.
- Prompt rules are a soft layer only. The real limits are the launch flags described in the README.

## Dependencies
`@playwright/mcp` is pinned to an exact version in `browser/package.json` and installed with `--ignore-scripts`. Version bumps get reviewed before they're merged.
