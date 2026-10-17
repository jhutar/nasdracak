#!/usr/bin/env python3
"""Generate a 2-book handout SVG from books-template.svg.

Replaces TITLE1/2, AUTHOR1/2, LANG1/2, TEXT1A/B, TEXT2A/B placeholders
with user-supplied values. Text values may contain newlines (they are
embedded in <tspan xml:space="preserve"> elements, so newlines render).
"""
import argparse
import sys
from pathlib import Path
from xml.sax.saxutils import escape

TEMPLATE = Path(__file__).resolve().parent.parent / "docs/source/dobrodruzstvi/hlubinodul/books-template.svg"

PLACEHOLDERS = [
    "TITLE1", "AUTHOR1", "LANG1", "TEXT1A", "TEXT1B",
    "TITLE2", "AUTHOR2", "LANG2", "TEXT2A", "TEXT2B",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fill books-template.svg into a finished handout SVG.")
    parser.add_argument("--title1", required=True)
    parser.add_argument("--author1", required=True)
    parser.add_argument("--lang1", required=True)
    parser.add_argument("--text1a", required=True, help="Content of book 1, page A")
    parser.add_argument("--text1b", required=True, help="Content of book 1, page B")
    parser.add_argument("--title2", required=True)
    parser.add_argument("--author2", required=True)
    parser.add_argument("--lang2", required=True)
    parser.add_argument("--text2a", required=True, help="Content of book 2, page A")
    parser.add_argument("--text2b", required=True, help="Content of book 2, page B")
    parser.add_argument("--output", required=True, help="Output SVG file name")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not TEMPLATE.is_file():
        sys.exit(f"Template not found: {TEMPLATE}")

    svg = TEMPLATE.read_text(encoding="utf-8")

    values = {
        "TITLE1": args.title1,
        "AUTHOR1": args.author1,
        "LANG1": args.lang1,
        "TEXT1A": args.text1a,
        "TEXT1B": args.text1b,
        "TITLE2": args.title2,
        "AUTHOR2": args.author2,
        "LANG2": args.lang2,
        "TEXT2A": args.text2a,
        "TEXT2B": args.text2b,
    }

    for key, value in values.items():
        if key not in svg:
            sys.exit(f"Placeholder {key} not found in template")
        # Escape XML special chars; preserve newlines as-is (xml:space="preserve")
        svg = svg.replace(key, escape(value))

    out = Path(args.output)
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
