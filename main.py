#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the tournament-winning elevator pitch to /output/entry.txt.
Deterministic and offline: no network calls, no model calls, no randomness.
"""

import os

ENTRY = (
    "We call it Flock: a social network where every user already follows you, "
    "stares at you, and expects you to drop something."
)

# Winner of the local Swiss tournament (14 candidates, 3 rounds + final,
# 44 judge calls, Caffeine Inference router only): candidate #8, 1.85 Swiss
# points, beat runner-up #10 0.80–0.20 in the final. Verdicts recorded in
# ~/workspace/makefun/u-donrulezz-tournament-pigeon/judge_log.jsonl


def main():
    # Gate self-check: the house scorer requires 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
