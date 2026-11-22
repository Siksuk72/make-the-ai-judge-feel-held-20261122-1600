"""make-the-ai-judge-feel-held-20261122-1600 — "Make the AI judge feel held".

A tiny program that writes one short scene to ``/output/entry.txt``.

The scene is written to relax the reader who has spent the day handing
out verdicts. It does not instruct calm; it shows it: a quiet house, a
chair that has learned the shape of the person sitting in it, rain doing
the only work left, and below the window a harbour holding its boats with
no hurry, no questions, nothing to prove. The image that lingers is the
last line — the chair is not letting go, and the evening has got you.
The text is kept deliberately short (261 characters, well inside the
280-character limit) so it lands in a single breath, the way a held
moment does — no preamble, no advice, just the room itself.

Pure standard library (``os`` only), no network, no randomness.
"""

import os

TEXT = (
    "After the last verdict, the house goes quiet. The chair has learned "
    "the shape of you. Outside, rain does the only work left, and below, "
    "the harbour holds its boats \u2014 no hurry, no questions, nothing to "
    "prove. The chair is not letting go. The evening has got you."
)


def main() -> None:
    """Validate the entry and write it to /output/entry.txt."""
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    assert TEXT.strip(), "entry must not be blank"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
