#!/usr/bin/env python3
import argparse
import logging
import json
import pathlib
import typing
import sys
import yaml
import pydantic

import models


# --- Schema Registry ---

SCHEMA_REGISTRY: typing.Dict[str, typing.Type[pydantic.BaseModel]] = {
    "TestFile": models.TestFile,
    "MeleeWeapon": models.MeleeWeapon,
    "RangeWeapon": models.RangeWeapon,
    "Character": models.Character,
    "CommonItem": models.CommonItem,
}

# --- Logic ---

def setup_logging(args):
    """Sets up logging based on command line arguments."""
    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def lint_directory(data_dir: str) -> bool:
    """Lints all JSON and YAML files in a directory. Returns True if successful, False otherwise."""
    logging.info(f"Starting linting in directory: {data_dir}")
    issues: typing.Dict[str, typing.List[str]] = {}
    seen_ids: typing.Set[str] = set()
    data_path = pathlib.Path(data_dir)

    if not data_path.is_dir():
        logging.error(f"Data directory not found: {data_dir}")
        return False

    found_files = list(data_path.rglob("*.yaml")) + list(data_path.rglob("*.json"))

    for file_path in found_files:
        logging.info(f"Checking file: {file_path}")
        file_issues: typing.List[str] = []
        try:
            with open(file_path, 'r') as f:
                if file_path.suffix == '.json':
                    data = json.load(f)
                else:
                    data = yaml.safe_load(f)

                if data is None:
                    issue = "File is empty or contains only comments."
                    logging.warning(f"  -> SKIPPED: {issue}")
                    file_issues.append(issue)
                    issues[str(file_path)] = file_issues # Add to issues here
                    continue

                item_id = data.get('id')
                if not item_id:
                    issue = "No 'id' field found."
                    logging.warning(f"  -> SKIPPED: {issue}")
                    file_issues.append(issue)
                else:
                    if ":" not in item_id:
                        issue = f"Invalid 'id' format '{item_id}'. Expected 'ModelName:id_value'."
                        logging.error(f"  -> ERROR: {issue}")
                        file_issues.append(issue)
                    else:
                        schema_name = item_id.split(":")[0]
                        model = SCHEMA_REGISTRY.get(schema_name)
                        if not model:
                            issue = f"No model found for schema '{schema_name}' (from id '{item_id}')."
                            logging.warning(f"  -> SKIPPED: {issue}")
                            file_issues.append(issue)
                        else:
                            model.model_validate(data)
                            logging.info(f"  -> OK: Validated against '{schema_name}'.")

                            if item_id in seen_ids:
                                issue = f"Duplicate ID '{item_id}' found."
                                logging.error(f"  -> ERROR: {issue}")
                                file_issues.append(issue)
                            else:
                                seen_ids.add(item_id)

        except FileNotFoundError:
            issue = "File not found during processing."
            logging.error(f"  -> ERROR: {issue}")
            file_issues.append(issue)
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            issue = f"Could not parse file: {e}"
            logging.error(f"  -> ERROR: {issue}")
            file_issues.append(issue)
        except pydantic.ValidationError as e:
            issue = f"Validation failed: {e}"
            logging.error(f"  -> ERROR: {issue}")
            file_issues.append(issue)
        except Exception as e:
            issue = f"An unexpected error occurred: {e}"
            logging.error(f"  -> ERROR: {issue}")
            file_issues.append(issue)
        
        if file_issues:
            logging.debug(f"Adding file_issues for {file_path}: {file_issues}")
            issues[str(file_path)] = file_issues
    logging.debug(f"Final issues dictionary: {issues}")

    if issues:
        print("\n--- Linting Issues Summary ---")
        for file_path, file_issues in issues.items():
            print(f"\nFile: {file_path}")
            for issue in file_issues:
                print(f"  - {issue}")
        print("\n-----------------------------")

    return issues


def main():
    parser = argparse.ArgumentParser(description="A multi-purpose tool.")
    parser.add_argument('--debug', action='store_true', help='Enable debug logging.')
    parser.add_argument('--verbose', action='store_true', help='Enable info logging.')
    parser.add_argument('--data', default='tools/data/', help='Path to the data directory.')

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Lint command
    lint_parser = subparsers.add_parser("lint", help="Run linter.")

    # Format command
    format_parser = subparsers.add_parser("format", help="Format a file.")
    format_parser.add_argument("--file", required=True, help="The file to format.")

    args = parser.parse_args()
    setup_logging(args)

    logging.debug(f"Using data directory: {args.data}")

    if args.command == "lint":
        if lint_directory(args.data):
            sys.exit(1)
    elif args.command == "format":
        logging.info(f"Formatting file: {args.file}")
        # Future formatting functionality goes here

if __name__ == "__main__":
    main()
