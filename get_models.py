"""Download the Kokoro voice model (about 115 MB) into models/ and check its SHA-256."""

import hashlib
import urllib.request
from pathlib import Path

URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
MODELS = Path(__file__).parent / "models"

for line in (MODELS / "SHA256SUMS.txt").read_text(encoding="utf-8-sig").splitlines():
    want, name = line.split()[:2]
    path = MODELS / name
    if not path.exists():
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(URL + name, path)
    got = hashlib.sha256(path.read_bytes()).hexdigest()
    if got.lower() != want.lower():
        path.unlink()
        raise SystemExit(f"{name}: checksum mismatch, file deleted. Try again.")
    print(f"{name}: OK")
