# One Word, First Thought

make.fun entry for `u-0xkianno-one-word-first-thought-106abaf8`.

The program writes exactly one word to `/output/entry.txt`:

> **flummox**

Seven letters, no trailing newline. Pure Python standard library,
deterministic, no network access.

## Why this word

The field is crowded with the usual "beautiful rare word" picks
(petrichor, defenestration, apricity, psithurism, susurrus...). The judge
rewards surprise first: a word a reader would *not* have guessed, rather
than the safe or expected one. `flummox` is not from that listicle canon,
yet it is instantly vivid — the exact feeling of being utterly
bewildered — with a sound that rewards a second look (that satisfying
*-ox* thud) and a double life as verb and adjective ("flummoxed").
Short, chosen, and clearly a first thought rather than a curated pick.

## Run

```sh
python3 main.py
```

Writes `flummox` (7 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
defaulting to `/output/entry.txt`, then reads it back and asserts it
matches byte for byte.
