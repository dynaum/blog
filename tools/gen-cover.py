#!/usr/bin/env python3
"""Generate a blog cover image with fal.ai (fal-ai/flux/dev).

The fixed flow for every post on blog.dynaum.com. The palette stays constant
across the series. Only the per-post concept changes.

Usage:
    set -a && source ~/.local_config && set +a   # loads FAL_KEY
    python3 tools/gen-cover.py <slug> "<concept sentence>"

Example:
    python3 tools/gen-cover.py 2026-05-29-did-it-actually-work \
      "A dark workshop bench at night, a single finished object under a warm amber lantern, a pair of polished calipers resting beside it mid-measurement"

Saves to src/assets/img/<slug>.png at 1344x768.
"""
import json
import os
import sys
import time
import urllib.request

MODEL = "fal-ai/flux/dev"
WIDTH, HEIGHT = 1344, 768

# The series palette. Constant across every post. Do not change per post.
PALETTE = (
    "Painterly digital illustration, deep near-black charcoal background, "
    "a warm honey-amber focal glow as the dominant light source, "
    "a muted teal-cyan rim light, brushstroke texture, soft bloom, "
    "cinematic composition, shallow depth of field. "
    "No text, no words, no letters, no logos."
)


def build_prompt(concept: str) -> str:
    return f"{concept.strip().rstrip('.')}. {PALETTE}"


def submit(prompt: str, key: str) -> dict:
    body = json.dumps({
        "prompt": prompt,
        "image_size": {"width": WIDTH, "height": HEIGHT},
        "num_inference_steps": 30,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": True,
        "output_format": "png",
    }).encode()
    req = urllib.request.Request(
        f"https://fal.run/{MODEL}",
        data=body,
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    slug, concept = sys.argv[1], sys.argv[2]
    key = os.environ.get("FAL_KEY")
    if not key:
        print("FAL_KEY not set. Run: set -a && source ~/.local_config && set +a", file=sys.stderr)
        return 1

    prompt = build_prompt(concept)
    print(f"Model: {MODEL}  Size: {WIDTH}x{HEIGHT}")
    result = submit(prompt, key)
    url = result["images"][0]["url"]

    out = os.path.join("src", "assets", "img", f"{slug}.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as r, open(out, "wb") as f:
        f.write(r.read())
    size = os.path.getsize(out)
    print(f"Saved {out} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
