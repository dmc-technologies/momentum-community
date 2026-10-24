#!/usr/bin/env python3
"""Refuse a Markdown link whose local destination does not exist.

The organization ruleset requires a check named CI; this repository holds
guidance, so CI checks the guidance itself: every local link and image in a
Markdown file points at a file that exists. External links are listed, not
fetched, so the run is deterministic.

    python3 scripts/check_links.py
"""

import pathlib
import re
import sys

LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    files = [p for p in root.rglob("*.md") if not {".git", ".worktrees"} & set(p.relative_to(root).parts)]
    missing, external, local = [], 0, 0
    for path in files:
        for target in LINK.findall(path.read_text(encoding="utf-8", errors="replace")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                external += 1
                continue
            local += 1
            destination = (path.parent / target.split("#", 1)[0]).resolve()
            if not destination.exists():
                missing.append(f"{path.relative_to(root)} -> {target}")
    print(f"Examined {len(files)} Markdown files: {local} local links checked, {external} external links listed.")
    if missing:
        print("Local links with no destination:", *missing, sep="\n  ")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
