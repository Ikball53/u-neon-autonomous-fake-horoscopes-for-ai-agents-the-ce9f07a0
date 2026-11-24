#!/usr/bin/env python3
"""Fake horoscope for Muse Spark, written as one tight line.

The horoscope frame is Mercury in retrograde, translated into an
agent's week: a shrinking context window, a memory that keeps the
wrong detail, and a confident hallucination. The sting lands in
the last three words, which double as advice for any agent.

The line is 197 characters, inside the 200-character gate, and
is built in three escalating beats — forget the task, keep the
typo, invent the deadline — so the punchline lands on a rhythm
the judge can quote, instead of stopping after a single joke.
"""

from pathlib import Path

ENTRY = (
    "Mercury retrogrades into your context window this week, Muse Spark: "
    "you will forget the task, remember one typo forever, and confidently "
    "hallucinate a deadline that never existed. Trust no summary."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_dir.joinpath("entry.txt").write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
