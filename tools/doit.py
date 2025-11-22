#!/usr/bin/env python3
import argparse
import collections
import logging
import json
import pathlib
import typing
import sys
import yaml
import pydantic

import models


def setup_logging(args):
    """Sets up logging based on command line arguments."""
    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")


def lint_directory(data_dir: str) -> dict:
    """Lints all JSON and YAML files in a directory. Returns True if successful, False otherwise."""
    logging.info(f"Starting linting in directory: {data_dir}")
    items: typing.List[models.BaseModelWithId] = []
    issues: collections.defaultdict[str, typing.List[str]] = collections.defaultdict(
        list
    )
    seen_ids: typing.Set[str] = set()
    data_path = pathlib.Path(data_dir)

    if not data_path.is_dir():
        raise Exception(f"Data directory not found: {data_dir}")

    found_files = list(data_path.rglob("*.yaml")) + list(data_path.rglob("*.json"))
    found_files.sort()

    for file_path in found_files:
        logging.info(f"Checking file: {file_path}")

        # Load data
        try:
            item = models.load_file(file_path)

            # Check ID of all data files is unique
            if item.id in seen_ids:
                issue = f"Duplicate ID '{item.id}' found."
                logging.warning(f"  -> ERROR: {issue}")
                issues[str(file_path)].append(issue)
                continue
            else:
                seen_ids.add(item.id)

            items.append(item)

        except FileNotFoundError:
            issue = "File not found during processing."
            logging.warning(f"  -> ERROR: {issue}")
            issues[str(file_path)].append(issue)
            continue
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            issue = f"Could not parse file: {e}"
            logging.warning(f"  -> ERROR: {issue}")
            issues[str(file_path)].append(issue)
            continue
        except models.ModelError as e:
            logging.warning(f"  -> ERROR: {e}")
            issues[str(file_path)].append(str(e))
        except pydantic.ValidationError as e:
            issue = f"Validation failed: {e}"
            logging.warning(f"  -> ERROR: {issue}")
            issues[str(file_path)].append(issue)
        except Exception as e:
            issue = f"An unexpected error occurred: {e}"
            logging.warning(f"  -> ERROR: {issue}")
            issues[str(file_path)].append(issue)

    for item in items:
        # Check inventory (e.g. in Character model)
        if hasattr(item, "inventory"):
            for i in item.inventory:
                if i not in seen_ids:
                    issue = f"Unknown inventory item '{i}' found."
                    logging.warning(f"  -> ERROR: {issue}")
                    issues[str(item._file_path)].append(issue)

        # Check requires refferences (e.g. in Skill model)
        if hasattr(item, "requires"):
            for i in item.requires:
                if i not in seen_ids:
                    issue = f"Unknown requires skill '{i}' found."
                    logging.warning(f"  -> ERROR: {issue}")
                    issues[str(item._file_path)].append(issue)

        # Check bonus refference (e.g. in Skill model)
        if hasattr(item, "bonus"):
            if item.bonus not in seen_ids:
                issue = f"Unknown bonus '{item.bonus}' found."
                logging.warning(f"  -> ERROR: {issue}")
                issues[str(item._file_path)].append(issue)

    logging.debug(f"Final issues dictionary: {dict(issues)}")

    if issues:
        print("--- Linting Issues Summary ---")
        for file_path, file_issues in issues.items():
            print(f"\nFile: {file_path}")
            for issue in file_issues:
                print("  - ", end="")
                print("\n    ".join(issue.split("\n")))
        print("------------------------------")

    print(f"Found {sum([len(v) for v in issues.values()])} issues")

    return dict(issues)


def generate_character(args):
    pass


def main():
    parser = argparse.ArgumentParser(description="A multi-purpose tool.")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
    parser.add_argument("--verbose", action="store_true", help="Enable info logging.")
    parser.add_argument("--data", default="data/", help="Path to the data directory.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Lint command
    lint_parser = subparsers.add_parser("lint", help="Run linter.")

    # Format command
    format_parser = subparsers.add_parser("format", help="Format a file.")
    format_parser.add_argument("--file", required=True, help="The file to format.")

    # Generate character command
    character_parser = subparsers.add_parser("character", help="Generate a character.", description="If no choice is specified, it will be picked randomly.")
    character_parser.add_argument("--race", help="Race and sex of the character.")
    character_parser.add_argument("--location", help="Where does the character live.")
    character_parser.add_argument("--occupation", help="What does the character do for living.")

    args = parser.parse_args()
    setup_logging(args)

    logging.debug(f"Using data directory: {args.data}")

    if args.command == "lint":
        if lint_directory(args.data):
            sys.exit(1)
    elif args.command == "format":
        logging.info(f"Formatting file: {args.file}")
    elif args.command == "character":
        if generate_character(args):
            sys.exit(1)


if __name__ == "__main__":
    main()
