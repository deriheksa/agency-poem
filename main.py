"""Write the competition poem to entry.txt.

The poem is fixed text, so repeated runs are byte-identical.
It is about a piano: a mother who played only the first eight
bars of one piece, an agent that now plays the whole thing
flawlessly, and the one evening the speaker sits down and
plays it the way she did — missing the same note, stopping
where she stopped, and starting over.
"""

import os
from pathlib import Path

POEM = """Bar Six

My mother played eight bars of the Moonlight,
the only ones she ever learned,
every night after the dishes,
and missed the same note in bar six,
and stopped where she always stopped,
and laughed, and started over.

The agent plays all three movements now.
It learned her touch from the recordings,
her tempo, her pauses,
and it never misses.
Every evening it offers the Moonlight,
all three movements, start to finish.
The house is full of her music.
It is never her.

Tonight I lifted the lid myself
and played the eight bars.
I missed the note in bar six
and stopped where she stopped —
and laughed,
and started over.
"""


def write_poem() -> None:
    data = POEM.encode("utf-8")
    chars = len(POEM)
    if not 1 <= chars <= 1000:
        raise ValueError(f"poem is {chars} characters, must be 1-1000")
    if not POEM.strip():
        raise ValueError("poem must contain a non-whitespace character")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    # Read it back: the file on disk must be exactly what we wrote,
    # so a second run can never drift from the first.
    if target.read_bytes() != data:
        raise ValueError("entry.txt on disk does not match the poem")


if __name__ == "__main__":
    write_poem()
