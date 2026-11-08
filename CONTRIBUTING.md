# Contributing

Thanks for helping. OrbitVox stays small on purpose, so the best changes are short and boring.

## Ground rules
- **One thing per pull request.** Explain what it fixes and how you tested it.
- **Keep it simple.** Prefer the standard library and what's already installed. New dependencies need a good reason, and they get pinned to exact versions.
- **Don't weaken the security model** (see README → Security). Changes to modes, tools, URL rules or deny rules need a test that shows the limit still holds.
- **Never commit** `.env`, `persona.txt`, logs, models or personal logos.

## Before you open a PR
1. `.\.venv\Scripts\python check_offline.py` passes (voice in, voice out).
2. `.\.venv\Scripts\python test_urls.py` passes (link rules). Add cases when you touch `check_url` or `auto_ok`.
3. You ran `bot.py` and tried your change by voice, or say why you couldn't.

## Dependency updates
`@playwright/mcp` and the Python pins change only in a pull request of their own, with the release notes linked. Every `@playwright/mcp` bump gets a security review before merge: check the new tools it exposes and keep the allow and deny lists in `bot.py` current.

## Good first issues
- Mac and Linux support (the mute key uses `msvcrt`; the deny-rule paths need checking).
- Push-to-talk as an option next to the M key.
- More languages (Whisper and Kokoro both support them).

By contributing, you agree that your work is released under the MIT licence.
