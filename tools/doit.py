#!/usr/bin/env python3
import argparse
import logging

def setup_logging(args):
    """Sets up logging based on command line arguments."""
    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="A multi-purpose tool.")
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')
    parser.add_argument('--verbose', action='store_true', help='Enable info logging.')
    parser.add_argument('--data', default='data/', help='Path to the data directory.')

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Lint command
    lint_parser = subparsers.add_parser("lint", help="Run linter.")

    # Format command
    format_parser = subparsers.add_parser("format", help="Format a file.")
    format_parser.add_argument("--file", required=True, help="The file to format.")

    args = parser.parse_args()
    setup_logging(args)

    logging.info(f"Using data directory: {args.data}")

    if args.command == "lint":
        logging.info("Running lint...")
        logging.debug("This is a debug message for lint.")
        # Future linting functionality goes here
    elif args.command == "format":
        logging.info(f"Formatting file: {args.file}")
        # Future formatting functionality goes here

if __name__ == "__main__":
    main()
