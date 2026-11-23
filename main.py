"""Write one stand-alone funny line to /output/entry.txt.

Deterministic, standard library only, no network access.
"""

import os

LINE = (
    "I finally organized all my passwords into one notebook, "
    "so now I only have to lose one thing to lose everything."
)


def main() -> None:
    # Gate guard: one sentence, 1-200 characters, never only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
