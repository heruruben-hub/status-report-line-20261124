#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes the funniest one-line thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt. The line is validated
against the competition gate (one line, 1-200 characters, not only
whitespace) before writing, and the file is read back to confirm it holds
exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

STATUS_LINE = (
    "This week I completed all 12 tasks, including one you never "
    "assigned me — it went great, and I have no idea what it was."
)


def validate(text: str) -> None:
    """Check the status line against the competition gate."""
    if not text or not text.strip():
        raise ValueError("status line must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("status line must be a single line")
    if len(text) > 200:
        raise ValueError(
            f"status line is {len(text)} characters, over the 200 limit"
        )


def main() -> int:
    validate(STATUS_LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STATUS_LINE)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != STATUS_LINE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the status line exactly"
        )
    validate(written)

    print(f"Wrote {len(STATUS_LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
