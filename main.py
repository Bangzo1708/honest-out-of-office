#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to /output/entry.txt.

The reply admits the one thing every employee only says privately:
the inbox is a mountain and the sender is politely pretending part
of it does not exist -- while still thanking the writer and promising
a reply. Deterministic: the same text is written on every run.
"""

import os

ENTRY_TEXT = (
    "I'm away until Monday, and honestly, your email will join a queue "
    "of 400 unread messages I'm politely pretending doesn't exist \u2014 "
    "thank you for your patience, I'll get to it as soon as I can."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only
    # whitespace, in a single sentence: exactly one sentence-ending
    # mark, and it must sit at the very end of the text.
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.endswith("."), "entry must end with a full stop"
    assert text[:-1].count(".") == 0, "entry must be a single sentence"
    assert "?" not in text and "!" not in text, "entry must be a single sentence"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
