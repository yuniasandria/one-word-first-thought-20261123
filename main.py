#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that comes to mind, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The word: flummox.
Pure Python standard library, deterministic, no network, no input.
"""

import os

WORD = "flummox"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    if not 1 <= len(data) <= 24:
        raise SystemExit("word outside the 1-24 character gate")
    if WORD != WORD.strip() or any(ch.isspace() for ch in WORD):
        raise SystemExit("word is not a single clean token")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("read-back mismatch: entry.txt is not the word")


if __name__ == "__main__":
    main()
