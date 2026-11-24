#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original one-line office joke to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(default ``/output/entry.txt``).

Standard library only, deterministic, no network. The program re-reads the file
it wrote and asserts the gate: UTF-8 text of 1 to 200 characters, not only
white space, exactly one line, no trailing newline.
"""

import os

JOKE = (
    "I declined the meeting invite, so Outlook booked a meeting "
    "to discuss why I declined the meeting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)

    # Write exactly the joke: one line, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Read-back validation against the gate in RULES.txt.
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert text == JOKE, "read-back differs from the selected joke"
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


if __name__ == "__main__":
    main()
