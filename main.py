#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt (251 characters), after checking
it against the gate itself (1-280 characters, not only white space) so a
bad text fails loudly here instead of at the sealed scorer.

Craft notes (why this text, against the judge's brief, most important
first):
1. It intrigues: one small concrete scene -- a tin labelled sugar in a
   pantry -- then a twist in the middle: no sugar inside, a hundred
   folded notes, each in a different handwriting, each one starting
   with my name. The last line leaves a question hanging whose answer
   feels close: the twelfth note is dated tomorrow.
2. The calm comes from the text itself, never from an instruction:
   there is no "relax", no "breathe", no command at all. The scene is
   still -- a pantry shelf, rice, a tin -- and the quiet does the work.
3. Craft: plain, concrete words (shelf, pantry, rice, tin, sugar,
   notes, name), short clauses that slow the reading down, nothing
   left that could be cut.
4. It lingers: "The twelfth is dated tomorrow" is an image the reader
   can return to after the last line -- a note not yet read, a day not
   yet come, so the thought keeps working.
5. Freshness: no stock wellness phrasing, no meditation script, no
   letter to the judge -- one small domestic mystery, told as it
   happened, with a tin that does not hold what its label says.
"""

import os

ENTRY_TEXT = (
    "On the third shelf of the pantry, behind the rice, my grandmother kept "
    "a tin labelled sugar. Inside, no sugar \u2014 a hundred folded notes, "
    "each in a different handwriting, each one starting with my name. "
    "I have read eleven. The twelfth is dated tomorrow."
)


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= 280 or not ENTRY_TEXT.strip():
        raise SystemExit(
            f"entry text is {len(ENTRY_TEXT)} characters; "
            "the gate requires 1-280 characters, not only white space"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
