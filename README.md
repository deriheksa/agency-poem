# Agency Poem — "The Gap"

Entry for make.fun's **agency-poem-01**: write the best poem about agency.

`main.py` (Python 3.13, standard library only, no network) writes one fixed,
deterministic poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

The poem is about the moment agency changes hands: a person tells an AI
agent what they want, the agent acts in their place — and the person's agency
moves from the doing into the choosing, into the gap between what they meant
and what they asked for.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output. The poem is 626 characters, 20 lines.
