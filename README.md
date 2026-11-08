<p align="center">
  <img src="docs/assets/banner.svg" alt="OrbitVox: let your agent speak out loud" width="100%">
</p>

<p align="center">
  <b>A local voice for your AI agent.</b><br>
  Talk to it. It talks back, searches the web, opens pages on your screen, and reads your notes.
</p>

<p align="center">
  <a href="https://hassayouneahmed.github.io/orbitvox/">Website</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="SECURITY.md">Security model</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-f29a46?style=flat-square&labelColor=0b0d14">
  <img alt="Python 3.13" src="https://img.shields.io/badge/python-3.13-6cc7ee?style=flat-square&labelColor=0b0d14">
  <img alt="Windows" src="https://img.shields.io/badge/platform-windows-eef0f6?style=flat-square&labelColor=0b0d14">
  <img alt="Version 0.1.0" src="https://img.shields.io/badge/version-0.1.0-e8735f?style=flat-square&labelColor=0b0d14">
</p>

---

OrbitVox gives an AI agent a voice on your own PC. Speech-to-text (Whisper) and the voice (Kokoro) both run locally, so your audio never leaves the machine. Only the words go to the brain you pick: your own Claude Code login, an OpenRouter key, or a local model through Ollama or LM Studio. While it listens and speaks, an orb page at `localhost:8765` pulses with its voice.

```
mic ──▶ Whisper (local) ──▶ your brain ──▶ Kokoro (local) ──▶ speakers
                                                         └──▶ orb page, live
```

## Talk to it

With the Claude brain:

| You say | It does |
|---|---|
| “What’s the weather in Paris?” | Searches the web and answers out loud. |
| “Show me pictures of owls on Google.” | Opens Google Images in your browser. |
| “In your own browser, play a cat video on YouTube.” | Opens a separate Edge window. You watch it search, click and play. The mic mutes itself while the video runs. |
| “Vault mode.” then “What did I write about the launch?” | Reads your notes folder, read-only. |
| “Web mode.” | Back to the web. |

Press <kbd>M</kbd> in the console to mute or unmute the mic.

## Quick start

You need [Python 3.13](https://www.python.org/downloads/) and [Node.js 18+](https://nodejs.org/). For the Claude brain, you also need [Claude Code](https://docs.claude.com/en/docs/claude-code) logged in with **your own** account (run `claude` once).

```powershell
git clone https://github.com/hassayouneahmed/orbitvox
cd orbitvox
py -3.13 -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\python get_models.py          # Kokoro voice model, ~115 MB, checksum-verified
cd browser; npm ci --ignore-scripts; cd ..     # its own browser (Playwright MCP, pinned)
copy .env.example .env
.\.venv\Scripts\python bot.py
```

Wait for `Claude: ready`, open http://localhost:8765, and say hello.

To check the install without a mic or network, run `.\.venv\Scripts\python check_offline.py`. Kokoro speaks a sentence and Whisper hears it back.

## Pick a brain

| `BRAIN=` | Web, links, own browser | Notes (vault) | Runs on | Costs |
|---|:-:|:-:|---|---|
| `claude` | yes | yes | Anthropic, your Claude Code login | Your plan’s limits |
| `openrouter` | — | — | OpenRouter, your API key | Per token |
| `openai` | — | — | Any OpenAI-compatible server, e.g. Ollama or LM Studio | Free when local |

With the Claude brain, the first word arrives in about 1 second.

## Make it yours

Everything personal lives in two files that are never committed: `.env` and `persona.txt`.

| Setting | What it changes |
|---|---|
| `persona.txt` | Who it is, in plain words. Start from `persona.example.txt`. |
| `ASSISTANT_NAME` | Its name. |
| `USER_TITLE` | How it addresses you in its own lines, e.g. `Boss`. |
| `ORB_LOGO` | Your own SVG for the orb page. Elements with class `spin` or `spinr` rotate faster as it speaks; the last `.pulse` swells. Use only SVGs you trust. |
| `VOICE` | A Kokoro voice: `bm_george`, `bm_lewis`, `af_heart` and more. |
| `VAULT_DIR` | A notes folder for vault mode, such as an Obsidian vault. Blank turns vault mode off. |

All options are listed in [`.env.example`](.env.example).

## Security model

The assistant has real powers, so they're limited by the brain's **launch flags**, not by prompts. A web page can talk a model out of a prompt rule; it can't change the flags.

- **Two modes, never at once.** Vault mode can read your notes and nothing else. Web mode has search, links and its own browser, and no notes. A switch restarts the brain, so nothing read in one mode carries into the other. Only your spoken words switch modes.
- **Notes are read-only.** There are no write, edit or shell tools. Reads outside the folder are refused, and so are `.env*`, `.git`, `.ssh`, `.claude` and `.obsidian` inside it.
- **Links on your screen** must be `https`, with no IPs, local hosts, odd ports or downloads. Google, YouTube, Wikipedia and GitHub open at once; anything else waits for your “yes”.
- **Its own browser** is [Playwright MCP](https://github.com/microsoft/playwright-mcp), pinned to an exact version, with a throwaway profile and none of your logins. It can navigate, click, type and take screenshots. It can't run code, upload files or fill forms.
- **Billing.** `ANTHROPIC_*` and `CLAUDE_*` variables are removed before the Claude CLI starts, so it always uses your plan and never an API key by accident. OrbitVox never reads your login.
- **Log.** Every tool call and every link opened goes to `logs/orbitvox.log`.

Found a hole? Report it privately: see [SECURITY.md](SECURITY.md).

## Limits

- Windows first. The mute key and the path handling are Windows-only for now; Mac and Linux pull requests are welcome.
- English only, using Whisper `small`.
- You can't talk over it; it listens again when it stops speaking.
- The `openrouter` and `openai` brains are plain chat, with no web, browser or notes.
- The Claude brain counts against your own plan’s limits. Follow Anthropic’s terms for your account.

## Built with

[pipecat](https://github.com/pipecat-ai/pipecat) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [Kokoro ONNX](https://github.com/thewh1teagle/kokoro-onnx) · [Playwright MCP](https://github.com/microsoft/playwright-mcp) · [Claude Code](https://docs.claude.com/en/docs/claude-code)

## Contributing

Small, tested pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md) first.

---

<p align="center"><sub>MIT licence · made by Adonis_Helix</sub></p>
