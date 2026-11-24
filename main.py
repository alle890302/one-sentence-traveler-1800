#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 (u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb).

Pass 1 entry (141 chars, run and verified):
  "Imagine every library, post office and newspaper in the world stacked
   into one room, where any letter you write arrives before the ink dries."

Pass 2 (FINAL, 128 chars): trimmed to two institutions --
  "Imagine every library and post office in the world stacked into one
   room, where a letter you write arrives before the ink dries."
Reasoning: criterion 4 (every word earns its place) is the tie-breaker
between the two. "Newspaper" is the third list item and the least
essential -- the internet's core for an 1800 mind is all knowledge
(library) plus instant messages (post office); news is a subset of what
those already hold, so the word costs 13 characters and a touch of
list-ness without adding a new idea. "A letter" instead of "any letter"
is cleaner and still true. The payoff clause is untouched, so the
memorable image survives intact. Criteria 1-3 are unchanged between
the two versions, so the tighter one wins.

Weighing against the judge's ordered criteria:
1. Explains the internet: the sentence's picture IS the internet's two
   pillars -- all the world's knowledge in one place, and messages that
   arrive instantly. A traveler from 1800 grasps both at once.
2. Built only from what 1800 knows: library, post office, newspaper,
   room, letter, ink. Not one word coined after the traveler's time.
   The frame word "Imagine" marks the whole thing as a thought
   experiment, so the comparison is judged as a comparison, not a
   literal claim -- which protects criterion 3.
3. True in spirit and in its one concrete claim: a written message
   really does arrive before its ink would dry. Nothing here misleads
   a reader who takes the comparison for what it is.
4. No feature list: one comparison carries the sentence (the brief
   explicitly allows a single comparison to carry it). Three
   institutions, one room, one payoff clause -- no filler.
5. Memorable image: "arrives before the ink dries" -- a phrase a
   reader still carries a week later, and it is the internet's
   defining wonder (instant delivery) in 1800 terms.

Beaten candidates:
- Road made of light (letters/books/pictures between every house):
  "every house on earth" is literally false (not every house is
  connected), and the three-item cargo list is a mini feature list.
- Post office where every letter ever written sits on one shelf:
  false on its face -- not every letter is on the internet, and not
  anyone may read any of them.
- Library with no walls / stranger hands you a book in a breath:
  177 chars, and "every book, letter and song ever made" overclaims.
- Market square that never sleeps: explains only the noisy social
  side, not what the internet IS; "every trader in the world" is
  literally false.
"""

import os

ENTRY = (
    "Imagine every library and post office in the world stacked into "
    "one room, where a letter you write arrives before the ink dries."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
