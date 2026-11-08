# Security

OrbitVox gives an AI model real powers on your computer: web, links, a browser and your notes. Security reports are very welcome.

## Reporting a problem
Please **don't open a public issue** for a security hole. Use GitHub's **private vulnerability reporting** instead: the Security tab → "Report a vulnerability". Include:
- what you did (steps, or the page or note that triggered it),
- what happened, and what should have happened,
- your OrbitVox version, your Claude Code version, and your brain (`claude`, `openrouter` or `openai`).

We aim to reply within 7 days.

## In scope
- Notes leaking into web mode, or the web reaching notes in vault mode.
- Reads outside the notes folder, or of the blocked files (`.env*`, `.git`, `.ssh`, `.claude`, `.obsidian`).
- Text on a web page or in a note that makes the assistant open a link, switch modes, or use a tool it shouldn't.
- Links that bypass the URL rules: IPs, local hosts, odd ports, downloads, or redirects that open without your "yes".
- Requests to the orb page from anything other than `localhost` / `127.0.0.1`.
- Any way the Claude CLI could pick up an API key from the environment.

## How the limits work
- Vault and web are separate modes with different launch flags, and a mode switch restarts the brain. That boundary doesn't depend on the model behaving.
- The notes-folder limits come from Claude Code's own permission rules (`--add-dir`, `permissions.deny`). They're tested on Windows; re-test them after a Claude Code update, because the CLI's behaviour can change.
- Prompt rules ("never log in", "never visit local addresses") are a soft extra layer only.

## Known limits (accepted for now)
- **The mic hears everything.** A mode switch or a "yes" is taken from what the mic hears, so sound from your speakers (a video, a call) counts as you. Use headphones, or press M to mute. The mic also mutes itself when its own browser lands on a video site.
- **Its own browser** can be steered by a web page to local addresses. It can only browse and click there, with a throwaway profile, and you see the window. It can type into fields one at a time, so it could fill a form if a page convinces it to; it has no file upload and can't run page scripts.
- **The Claude account.** OrbitVox uses whichever account the Claude Code CLI is logged in to.

## Dependencies
`@playwright/mcp` is pinned to an exact version in `browser/package.json` and installed with `--ignore-scripts`. Every version bump gets a security review before it's merged. Kokoro model files are checked against SHA-256 values recorded from our first download (the upstream release publishes none).
