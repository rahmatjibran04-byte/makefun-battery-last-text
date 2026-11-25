#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger - make.fun bounty entry.

A deterministic program (Python standard library only) that writes one
line -- the phone battery's last text to the charger it waited for all
day -- to /output/entry.txt.

The joke is a breakup text, not a dying-battery complaint: the battery
waited all day, the charger finally shows up at 1% acting like a hero,
and the battery answers that it was fine dying, because at least dying
never left it on read. The punchline lands in the final words, in the
voice of someone actually typing a furious last text -- needy, spiteful,
and done waiting.

Usage:
    python3 main.py

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT environment variable (used only for local testing).
"""

import os

ENTRY = (
    "I waited all day. You finally plug me in at 1% and act like you "
    "saved me. I was fine dying \u2014 at least dying never left me on read."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    # Create the output directory only if it is missing; never chmod a
    # directory we did not create ourselves (in particular, never /output).
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone. Only chmod a file this program wrote itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
