#!/usr/bin/env python3
"""Roast Your Fridge entry: one line, written to /output/entry.txt."""

import os
import sys


def roast() -> str:
    return (
        "My fridge beeps if the door stays open for ten seconds, "
        "which is the closest thing in this house to someone noticing I am gone."
    )


def main() -> int:
    line = roast()
    if not line.strip() or len(line) > 200:
        return 1
    if any(ord(ch) < 32 and ch not in "\t" for ch in line):
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
