"""Write one poem about agency to entry.txt.

The poem is fixed and deterministic: the same bytes on every run.
It is about the moment agency changes hands — when a person tells an
AI agent what they want, and the agent acts in their place.
"""

import os
from pathlib import Path

POEM_LINES = [
    "I used to do it with my own hands —",
    "the letter, the call, the key in the door.",
    "Now I say what I want, in plain words,",
    "and it goes where I cannot follow.",
    "",
    "It never sleeps. It never asks why.",
    "It does exactly what I said.",
    "And in the space between the saying and the doing",
    "a small country opens: the gap",
    "between what I meant and what I asked for.",
    "",
    "That gap is mine. That gap is the work.",
    "I no longer hold the pen; I hold the question.",
    "My hand has left the wheel, but the wheel",
    "still turns where I pointed it.",
    "",
    "Agency was never the hand.",
    "It was the choosing, before the doing —",
    "the yes that stays yes",
    "when other hands carry it out.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
