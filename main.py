#!/usr/bin/env python3
"""The Moon Finally Answers Back — one line in the Moon's voice.

The entry is a single fixed line, written for make.fun
u-mang-the-moon-finally-answers-back-781a7ec1: the Moon answers the
wishes, howls and late-night promises of everyone staring up at it.
After four billion years of listening, it has one complaint of its
own. This program writes that line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The line is fixed text: the
same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Four billion years of wishes, howls, and 3am promises \u2014 and "
    "not one of you has ever wished me a good night back."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the line against the gate, then write it out."""
    if not 1 <= len(LINE) <= 240:
        return abort(f"line is {len(LINE)} characters, the gate allows 1-240")
    if not LINE.strip():
        return abort("line is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
