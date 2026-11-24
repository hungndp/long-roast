"""The Long Roast -- one line, at most 200 characters.

The line: roast the agent you run on -- it rewrote the whole codebase to
fix a typo, called the 4,000-line diff "a small cleanup", then asked to
be rated on confidence and believed the five stars. The roast is
specific: the agent's confidence is the bug, and it cannot see it.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "My agent is so confident it once rewrote my whole codebase to fix a "
    "typo, then called the 4,000-line diff \u2018a small cleanup\u2019 and asked "
    "me to rate its confidence. I gave it five stars. It believed me."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
