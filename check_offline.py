"""Offline self-check: Kokoro speaks a sentence, Whisper hears it back. No network, no mic."""

import time
from pathlib import Path

import resampy
import soundfile as sf
from faster_whisper import WhisperModel
from kokoro_onnx import Kokoro

HERE = Path(__file__).parent
TEXT = "Good evening. Your tea is ready in the library."

kokoro = Kokoro(str(HERE / "models/kokoro-v1.0.int8.onnx"), str(HERE / "models/voices-v1.0.bin"))
for voice in ("bm_george", "bm_fable", "bm_lewis"):
    t = time.time()
    audio, rate = kokoro.create(TEXT, voice=voice, lang="en-gb")
    sf.write(HERE / f"sample_{voice}.wav", audio, rate)
    print(f"{voice}: {len(audio) / rate:.1f}s of audio in {time.time() - t:.1f}s")

t = time.time()
whisper = WhisperModel("small", device="cpu", compute_type="int8")
# Pass an array like pipecat does (faster-whisper's file decoder breaks on av 19).
wav, sr = sf.read(HERE / "sample_bm_george.wav", dtype="float32")
segs, _ = whisper.transcribe(resampy.resample(wav, sr, 16000), language="en")
heard = " ".join(s.text.strip() for s in segs)
print(f"whisper heard: {heard!r} in {time.time() - t:.1f}s (incl. load)")
assert "tea" in heard.lower() and "library" in heard.lower(), heard
print("OK")
