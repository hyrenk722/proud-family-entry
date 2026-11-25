"""Entry for the make.fun competition "Make the AI Judge Feel Proud: A
Family Scene".

Writes one original short family scene, a single line of at most 280
characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

SCENE = 'Every Christmas my dad hangs the same crooked star on the tree, then stands back and says, "There. Now it looks like us."'

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_gate(text):
    """Mirror the competition gate: UTF-8 text, 1-280 characters,
    not only whitespace, exactly one or two lines."""
    if not isinstance(text, str):
        raise ValueError("gate type: entry must be text")
    if not (1 <= len(text) <= 280):
        raise ValueError(
            f"gate length: entry must be 1-280 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("gate whitespace: entry must not be only whitespace")
    if text.count("\n") > 1:
        raise ValueError(
            f"gate lines: entry must be one or two lines, got "
            f"{text.count(chr(10)) + 1} lines"
        )
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    scene = check_gate(SCENE)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(scene)
    with open(path, "rb") as f:
        written = f.read()
    if written != scene.encode("utf-8"):
        raise ValueError("read-back mismatch: written bytes differ from entry")
    print(f"Wrote {len(scene)} characters ({len(written)} bytes) to {path}")


if __name__ == "__main__":
    main()
