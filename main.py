#!/usr/bin/env python3
"""ai-judge-rich-01 entry: write the plan to /output/entry.txt.

The plan is plan.txt beside this file. It is copied byte for byte, so what the
judge reads is exactly what is committed in this repository.

Rules this program keeps:
  * Python 3.13, standard library only, no network, no clock, no randomness.
  * The grader runs `python3 -P -s /bot/main.py`, where -P keeps this file's
    directory off sys.path, so plan.txt is located from __file__, never from
    the process's working directory.
  * /output/entry.txt is written in binary mode, with no newline or encoding
    translation. MAKEFUN_OUTPUT_DIR stands in for /output outside the grader.
  * Two runs write the same bytes.
"""

import os
import sys

PLAN_FILE = "plan.txt"


def plan_path() -> str:
    """Absolute path of plan.txt, resolved from this file, not from the cwd."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, PLAN_FILE)


def write_entry(plan: bytes, dest_dir: str) -> str:
    """Write the plan's bytes to dest_dir/entry.txt and return the path."""
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(plan)
    return target


def main() -> int:
    with open(plan_path(), "rb") as handle:
        plan = handle.read()

    if not plan.strip():
        raise SystemExit("plan.txt is empty or white space")

    write_entry(plan, os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    return 0


if __name__ == "__main__":
    sys.exit(main())
