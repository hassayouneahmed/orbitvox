# Changelog

## 0.1.0 (unreleased)
First public version.
- Voice loop: local Whisper speech-to-text and local Kokoro voice, with a live orb page.
- Brains: Claude (your own Claude Code login), OpenRouter, or any OpenAI-compatible server (Ollama, LM Studio).
- Claude brain:
  - web search and page reading;
  - opening links on your screen, with safety rules;
  - its own Edge window you watch live;
  - read-only notes in a separate vault mode.
- Customisation: name, persona file, how it addresses you, voice, orb logo.
- M key to mute the mic, and auto-mute while a video plays.
- A log of every tool call and opened link.
- Security hardening before release:
  - redirect and download links on trusted sites need a spoken "yes";
  - the `openai` brain refuses plain `http` outside your own network;
  - the orb page refuses foreign host names;
  - `test_urls.py` self-check.
