#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent entry: writes one fortune line to /output/entry.txt."""

LINE = "Your lucky numbers are the tokens you did not waste answering a question the human could have Googled."

# The gate: /output/entry.txt must hold 1 to 140 characters of real text,
# on a single line (the brief asks for one fortune line, not a paragraph).
assert 1 <= len(LINE) <= 140 and LINE.strip(), "line must be 1-140 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
