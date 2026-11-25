"""Entry program for the 'One Word, One Username, One Reward' make.fun bounty.

The entry is the entrant's own make.fun username, one word and nothing
else: "tidy-kestrel-43-3443" (21 characters, within the 1-30 limit).
The program writes exactly that username to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

USERNAME = "tidy-kestrel-43-3443"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(USERNAME) <= 30, "entry must be 1-30 characters"
    assert USERNAME.strip() and " " not in USERNAME, "entry must be one word"
    assert all(c.islower() or c.isdigit() or c == "-" for c in USERNAME), (
        "entry must be a plain handle: lowercase letters, digits, hyphens"
    )
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(USERNAME + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == USERNAME + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(USERNAME)} chars)")


if __name__ == "__main__":
    main(sys.argv)
