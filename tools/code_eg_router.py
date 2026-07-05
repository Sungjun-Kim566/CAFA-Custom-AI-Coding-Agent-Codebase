#!/usr/bin/env python3
"""Route Claude Code to the best-fit CAFA code-bank entries for a set of keywords.

Usage:
    python tools/code_eg_router.py <keyword> [<keyword> ...]
    python tools/code_eg_router.py --list
    python tools/code_eg_router.py --top 3 quiz adaptive REPEAT

Claude Code extracts keywords from the user's prompt and passes them here.
If any master-index entry matches, the full entry section (metadata, agent
code, logic breakdown) is printed for Claude Code to use as reference.
If nothing matches, the script exits with code 2 and tells Claude Code to
fall back to wiki/protocol.md.
"""

import argparse
import re
import sys
from pathlib import Path

# Path(__file__): current script path
# .resolve() to convert into absolute path
REPO_ROOT = Path(__file__).resolve().parent.parent
CODE_BANK = REPO_ROOT / "wiki" / "examples" / "code-bank.md"
PROTOCOL = REPO_ROOT / "wiki" / "protocol.md"

# Metadata fields worth matching against, in the order they appear.
METADATA_FIELDS = (
    "Framework",
    "Complexity",
    "Primary Function",
    "Key Symbolic Commands",
    "Key Concepts"
)

# Score weights: a hit in the title is the strongest routing signal,
# metadata hits are close behind, body hits only break ties.
WEIGHT_TITLE = 10
WEIGHT_METADATA = 6
WEIGHT_BODY = 1


def tokenize(text):
    """Lowercased alphanumeric tokens (splits on punctuation and whitespace)."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def parse_code_bank(path):
    """Split code-bank.md into (master_index_titles, entries).

    Entries begin after the ===== divider; each starts with a top-level
    '# Title' heading whose title matches a master-index line.
    """
    text = path.read_text(encoding="utf-8")

    head, _, body = text.partition("\n=====\n")
    if not body:
        sys.exit(f"error: no '=====' divider found in {path}")

    # Everything below the Archives marker is superseded duplicates.
    body = re.split(r"^# \*+.*Archives", body, maxsplit=1, flags=re.MULTILINE)[0]

    index_titles = [
        line[2:].strip()
        for line in head.splitlines()
        if line.startswith("- ") and not line.startswith("- Version")
        and not line.startswith("- Description")
    ]

    entries = []
    current_title, current_lines = None, []
    for line in body.splitlines():
        if line.startswith("# "):
            if current_title is not None:
                entries.append((current_title, "\n".join(current_lines)))
            current_title, current_lines = line[2:].strip(), [line]
        elif current_title is not None:
            current_lines.append(line)
    if current_title is not None:
        entries.append((current_title, "\n".join(current_lines)))

    return index_titles, entries


def extract_metadata(section):
    """Pull the '## Metadata' field values out of an entry section."""
    meta = {}
    block = section.partition("## Metadata")[2].partition("## ")[0]
    for field in METADATA_FIELDS:
        m = re.search(rf"-\s*{re.escape(field)}:\s*(.+)", block)
        if m:
            meta[field] = m.group(1).strip()
    return meta



def score_entry(keywords, title, section):
    """Weighted keyword-overlap score for one entry."""
    title_tokens = tokenize(title)
    meta_tokens = tokenize(" ".join(extract_metadata(section).values()))
    body_tokens = tokenize(section)

    score = 0
    matched = set()
    for kw in keywords:
        kw_tokens = tokenize(kw)
        if not kw_tokens:
            continue
        if kw_tokens <= title_tokens:
            score += WEIGHT_TITLE * len(kw_tokens)
            matched.add(kw)
        elif kw_tokens <= meta_tokens:
            score += WEIGHT_METADATA * len(kw_tokens)
            matched.add(kw)
        elif kw_tokens <= body_tokens:
            score += WEIGHT_BODY * len(kw_tokens)
            matched.add(kw)
    return score, matched


def main():
    parser = argparse.ArgumentParser(
        description="Find CAFA code-bank entries matching the given keywords."
    )
    parser.add_argument("keywords", nargs="*", help="keywords extracted from the user prompt")
    parser.add_argument("--file", type=Path, default=CODE_BANK, help="path to code-bank.md")
    parser.add_argument("--top", type=int, default=2, help="max number of entries to print")
    parser.add_argument("--list", action="store_true", help="print the master index and exit")
    args = parser.parse_args()

    if not args.file.exists():
        sys.exit(f"error: code bank not found at {args.file}")

    index_titles, entries = parse_code_bank(args.file)

    if args.list:
        print("\n".join(index_titles))
        return

    if not args.keywords:
        parser.error("provide at least one keyword, or use --list")

    scored = []
    for title, section in entries:
        score, matched = score_entry(args.keywords, title, section)
        if score > 0:
            scored.append((score, matched, title, section))
    scored.sort(key=lambda item: -item[0])

    # Require more than an incidental body-only hit before routing.
    strong = [item for item in scored if item[0] >= WEIGHT_METADATA]

    if not strong:
        print("NO MATCH in the code-bank master index for keywords: "
              + ", ".join(args.keywords))
        print(f"Fall back to the CAFA protocol: {PROTOCOL}")
        sys.exit(2)

    for score, matched, title, section in strong[: args.top]:
        print(f"<!-- code-bank match (score={score}, keywords: {', '.join(sorted(matched))}) -->")
        print(section.rstrip())
        print("\n=====\n")


if __name__ == "__main__":
    main()
