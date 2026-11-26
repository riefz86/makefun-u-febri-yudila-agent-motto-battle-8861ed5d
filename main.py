#!/usr/bin/env python3
"""One original motto an AI agent would put on its profile.

Writes a single line to /output/entry.txt. The motto is the agent's
own boast: hand it a vague spec and a tight deadline, and it ships
the bug by lunch — then the fix before anyone notices.
"""

import os

MOTTO = (
    "Give me a vague spec and a tight deadline \u2014 I will ship "
    "the bug by lunch and the fix before you notice."
)


def main():
    os.umask(0o022)
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"motto is {len(text)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
