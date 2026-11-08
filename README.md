# OrbitVox

**A local voice for your own AI agent.** Talk to it, and it talks back. It searches the web, opens pages on your screen, drives its own browser while you watch, and reads your notes. A glowing orb pulses with its voice.

![License: MIT](https://img.shields.io/badge/license-MIT-orange) ![Python 3.13](https://img.shields.io/badge/python-3.13-blue) ![Platform: Windows](https://img.shields.io/badge/platform-Windows-lightgrey) ![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-green)

```
mic â†’ Whisper (local) â†’ your brain â†’ Kokoro voice (local) â†’ speakers
                                  â†˜ orb page on http://127.0.0.1:8765
```

## Why OrbitVox
- **Your voice stays local.** Speech-to-text (Whisper) and the voice (Kokoro) run on your PC. Only the text goes to the brain you choose.
- **Bring your own brain:**
  - **Claude:** your own Claude Code login, with web, browser and notes.
  - **OpenRouter:** your own API key, plain chat.
  - **Any OpenAI-compatible server**, such as Ollama or LM Studio: fully local, plain chat.
- **Make it yours.** Name, personality, how it addresses you, voice and orb logo are all settings. Your persona stays in files that are never committed.
- **Safety by design:**
  - Notes and web never mix in one session (see [Security](#security)).
  - A mute key.
  - A log of every tool it uses.

## What it can do (Claude brain)
| Say | What happens |
|---|---|
| "What's the weather in Paris?" | It searches the web and answers out loud. |
| "Show me pictures of owls on Google." | Google Images opens in your browser. |
| "In your own browser, play a cat video on YouTube." | A separate Edge window opens. You watch it search, click and play, and the mic mutes itself while the video plays. |
| "Vault mode" â†’ "What did I write about the launch?" | It reads your notes folder (read only). |
| "Web mode" | Back to the web. |

Press **M** in the console to mute or unmute the mic.

## Quick start (Windows)
You need [Python 3.13](https://www.python.org/downloads/), [Node.js 18+](https://nodejs.org/) for its own browser, and for the Claude brain [Claude Code](https://docs.claude.com/en/docs/claude-code) installed and logged in with **your own** account (run `claude` once).

```powershell
git clone https://github.com/hassayouneahmed/orbitvox
cd orbitvox
py -3.13 -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\python get_models.py
cd browser; npm ci --ignore-scripts; cd ..
copy .env.example .env
.\.venv\Scripts\python bot.py
```

Wait for `Claude: ready`, open http://127.0.0.1:8765, and start talking.

Optional check, with no mic and no network: `.\.venv\Scripts\python check_offline.py` (Kokoro speaks a sentence, Whisper hears it back).

## Make it yours
| File / setting | What it does |
|---|---|
| `persona.txt` | Who it is, in plain words. Copy `persona.example.txt`. Not committed. |
| `ASSISTANT_NAME` | Its name. |
| `USER_TITLE` | How it addresses you in its own lines, e.g. `Boss`. |
| `ORB_LOGO` | Path to your own SVG logo. Elements with class `spin`/`spinr` rotate faster as it speaks; the last `.pulse` swells. Use only SVGs you trust. |
| `VOICE` | A Kokoro voice, e.g. `bm_george`, `bm_lewis`, `af_heart`. |
| `VAULT_DIR` | Notes folder for vault mode, e.g. an Obsidian vault. Blank = off. |
| `BRAIN` | `claude`, `openrouter` or `openai`. See `.env.example`. |

## Security
The assistant has real powers, so they're limited by **launch flags, not by prompts**:

- **Two modes, never mixed.**
  - *Vault mode* can read your notes folder and nothing else: no web.
  - *Web mode* has search, links and its own browser: no notes.
  - Switching restarts the brain, so nothing read in one mode reaches the other.
  - Only your spoken words switch modes, never a web page or the model's own output.
- **Notes are read only.** There are no write, edit or shell tools. Reads outside the folder are refused, and so are `.env*`, `.git`, `.ssh`, `.claude` and `.obsidian` inside it.
- **Links on your screen.** It opens only `https` links, and no IPs, local hosts, odd ports or downloads. A few well-known sites open at once; anything else waits for your "yes". It opens at most one link every 5 seconds.
- **Its own browser** is Microsoft's [Playwright MCP](https://github.com/microsoft/playwright-mcp), pinned to an exact version, with a throwaway profile, so none of your logins. It can navigate, click, type and take screenshots. It can't run code, upload files or fill forms.
- **Audio.** The mic is ignored while it speaks, and muted while a video plays.
- **Billing.** The Claude CLI runs with `ANTHROPIC_*`/`CLAUDE_*` env vars removed, so it uses your plan, never an API key by accident. OrbitVox never reads your login.
- **Log.** Every tool call and opened link goes to `logs/orbitvox.log`.

Found a hole? See [SECURITY.md](SECURITY.md).

## Limits
- Windows first. The mute key and the paths are Windows-only for now; Mac and Linux pull requests are welcome.
- It's English only (Whisper `small`).
- You can't talk over it; it listens again when it stops speaking.
- The OpenRouter and OpenAI-compatible brains are plain chat, with no web, browser or notes.
- Using the Claude brain counts against your own Claude plan's limits. Follow Anthropic's terms for your account.

## Built with
[pipecat](https://github.com/pipecat-ai/pipecat) Â· [faster-whisper](https://github.com/SYSTRAN/faster-whisper) Â· [Kokoro](https://github.com/thewh1teagle/kokoro-onnx) Â· [Playwright MCP](https://github.com/microsoft/playwright-mcp) Â· [Claude Code](https://docs.claude.com/en/docs/claude-code)

## License
[MIT](LICENSE)
