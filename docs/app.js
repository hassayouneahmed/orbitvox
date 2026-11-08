// OrbitVox landing: meter readout, conversation re-enactment driving the orb, copy button.
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

// Meter: a static readout, heights from a two-peak envelope (speech-band shaped), not random noise.
const meter = document.getElementById("meter");
for (let i = 0; i < 72; i++) {
  const x = i / 71;
  const h = 0.12 + 0.8 * Math.exp(-((x - 0.3) ** 2) / 0.012) + 0.45 * Math.exp(-((x - 0.66) ** 2) / 0.02)
    + 0.08 * Math.sin(i * 1.7);
  const bar = document.createElement("span");
  bar.style.height = `${Math.min(100, Math.max(8, h * 100))}%`;
  bar.style.opacity = (0.35 + 0.65 * Math.min(1, h)).toFixed(2);
  meter.append(bar);
}

// Orb: rings speed up and the core swells while "Orbit" speaks.
const stage = document.getElementById("orb");
let rings = [];
requestAnimationFrame(() => {
  rings = stage.getAnimations({ subtree: true }).filter((a) => a.animationName === "spin");
});
let level = 0, target = 0;
function tick() {
  level += (target - level) * (target > level ? 0.35 : 0.08);
  stage.style.setProperty("--level", level.toFixed(3));
  list.style.setProperty("--level", level.toFixed(3));
  for (const a of rings) a.playbackRate = 1 + level * 7;
  requestAnimationFrame(tick);
}
if (!reduced) requestAnimationFrame(tick);

// Conversation: lines appear one by one; Orbit lines pulse the orb like real speech.
const list = document.getElementById("transcript");
const lines = [...list.children];
const button = document.getElementById("replay");
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
let playing = false;

async function play() {
  if (playing) return;
  playing = true;
  button.disabled = true;
  button.textContent = "Playing…";
  list.classList.add("is-playing");
  lines.forEach((li) => li.classList.remove("is-shown"));
  for (const li of lines) {
    li.classList.add("is-shown");
    const words = li.textContent.split(/\s+/).length;
    if (li.dataset.who === "orbit" && !reduced) {
      li.classList.add("is-speaking");
      const end = performance.now() + words * 260;
      while (performance.now() < end) {          // syllable-like bursts
        target = 0.55 + Math.random() * 0.45;
        await wait(110);
        target = 0.15;
        await wait(70);
      }
      target = 0;
      await wait(500);
      li.classList.remove("is-speaking");
    } else {
      await wait(reduced ? 150 : 600 + words * 120);
    }
  }
  playing = false;
  button.disabled = false;
  button.textContent = "Play it again";
}
button.addEventListener("click", play);

// Start the re-enactment once when the transcript scrolls into view.
new IntersectionObserver((entries, obs) => {
  if (entries.some((e) => e.isIntersecting)) { obs.disconnect(); play(); }
}, { threshold: 0.4 }).observe(list);

// Copy the install commands.
for (const btn of document.querySelectorAll("[data-copy]")) {
  btn.addEventListener("click", async () => {
    const text = document.getElementById(btn.dataset.copy).innerText;
    try {
      await navigator.clipboard.writeText(text);
      btn.dataset.state = "done";
      btn.textContent = "Copied";
    } catch {
      btn.dataset.state = "error";
      btn.textContent = "Select and copy";
    }
    setTimeout(() => { delete btn.dataset.state; btn.textContent = "Copy"; }, 2000);
  });
}
