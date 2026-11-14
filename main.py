"""Emit one short poem about agency to entry.txt.

The text is fixed: the program only writes it out, so every run
produces the same bytes. The poem is about a cook who hands the
cooking to an agent and takes back the tasting — the one mouthful
nobody asked for, where getting it wrong is still hers.
"""

from pathlib import Path
import os

TEXT = """The Tasting

My mother's recipe says a pinch.
The agent weighs it: 0.4 grams.
It watches the pot the way she never did,
thermometer in, lid on, timer set,
and the soup comes out exactly right
three times a week, without me.

It never tastes. That is not its job.
Its job is the numbers. Mine was
the spoon — the one mouthful standing up,
before the bowls come out, that says
too much, too little, enough.

Last Tuesday I stood at the stove
while it stirred, and reached in
with the wooden spoon and tasted.
Too much salt. I added water.
Then too little. I added salt again,
with my fingers, the way she did.

It said, gently, the salt is 0.6 now.
I said, I know. It waited, the way
good tools wait. I took the spoon back
and tasted again, and got it wrong
in the direction of her.
"""


def run() -> None:
    # The gate allows 1 to 1,000 characters; refuse to write otherwise.
    if not 1 <= len(TEXT) <= 1000:
        raise ValueError(f"poem is {len(TEXT)} characters, must be 1-1000")
    where = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    where.mkdir(parents=True, exist_ok=True)
    (where / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    run()
