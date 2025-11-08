#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="A multi-purpose tool.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Lint command
    lint_parser = subparsers.add_parser("lint", help="Run linter.")

    # Format command
    format_parser = subparsers.add_parser("format", help="Format a file.")
    format_parser.add_argument("--file", required=True, help="The file to format.")

    args = parser.parse_args()

    if args.command == "lint":
        print("Running lint...")
        # Future linting functionality goes here
    elif args.command == "format":
        print(f"Formatting file: {args.file}")
        # Future formatting functionality goes here

if __name__ == "__main__":
    main()
