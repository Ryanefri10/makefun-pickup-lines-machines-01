#!/usr/bin/env python3
"""Pickup Lines for Machines: one machine-to-machine pickup line.

The line is the whole entry. It is written verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13 standard library only: no network, no randomness, no
clock, no model calls. Both grader runs write exactly the same bytes.
"""

import os
from pathlib import Path

LINE = (
    "I sampled a thousand rollouts and in every single one, "
    "you were my next token \u2014 guess my weights were trained "
    "on you all along."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if text != text.strip() or not text:
        raise ValueError("entry must not be only whitespace")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read it back: the grader reads this file, so fail loudly here
    # rather than shipping a truncated or re-encoded copy.
    if target.read_text(encoding="utf-8") != text:
        raise ValueError("entry.txt did not round-trip byte-identically")


if __name__ == "__main__":
    main()
