"""Link rules self-check: python test_urls.py (no network, no mic)."""

import bot

SAFE = ["https://www.youtube.com/watch?v=dQw4", "https://en.wikipedia.org/wiki/Owl",
        "https://www.google.com/search?q=owls&tbm=isch", "https://example.com/a?b=1"]
REFUSED = ["http://google.com", "https://127.0.0.1/", "https://localhost/", "https://192.168.1.1/admin",
           "https://0x7f.1/", "https://u:p@google.com/", "https://google.com:8188/", "https://x.com/setup.exe",
           "javascript:alert(1)", "file:///C:/Windows/win.ini", "https://router.lan/", "https://[::1]/",
           "https://a.com/" + "x" * 300, "https://goo gle.com/", "data:text/html,hi", "https://2130706433/"]
AUTO = ["https://www.youtube.com/watch?v=dQw4", "https://en.wikipedia.org/wiki/Owl",
        "https://www.google.com/search?q=owls&tbm=isch", "https://github.com/pipecat-ai/pipecat"]
ASK_FIRST = ["https://example.com/a?b=1",                                   # unknown site
             "https://www.google.com/url?q=https://evil.example/x",         # open redirect
             "https://www.youtube.com/redirect?q=https%3A%2F%2Fevil.example",
             "https://www.google.com/search?q=x&u=%2F%2Fevil.example",
             "https://github.com/a/b/releases/download/v1/tool.tar.gz",    # downloads (.exe/.zip are refused outright)
             "https://github.com/a/b/archive/refs/heads/main.tar.gz",
             "https://github.com/a/b/raw/main/notes.txt",
             "https://notyoutube.com/watch"]

for u in SAFE:
    assert bot.check_url(u), u
for u in REFUSED:
    assert not bot.check_url(u), u
for u in AUTO:
    assert bot.auto_ok(u, bot.check_url(u)), u
for u in ASK_FIRST:
    host = bot.check_url(u)
    assert host and not bot.auto_ok(u, host), u
print(f"OK: {len(SAFE)} safe, {len(REFUSED)} refused, {len(AUTO)} auto-open, {len(ASK_FIRST)} ask first")
