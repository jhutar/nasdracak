#!/usr/bin/env python3
import argparse
import logging
import json
from pathlib import Path
from typing import Dict, Type, Literal

import yaml
from pydantic import BaseModel, Field, ValidationError

# --- Pydantic Models ---

class TestFile(BaseModel):
    schema_name: Literal["TestFile"] = Field(alias="$schema")
    name: str

# --- Schema Registry ---

SCHEMA_REGISTRY: Dict[str, Type[BaseModel]] = {
    "TestFile": TestFile,
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

def lint_directory(data_dir: str):
    """Lints all JSON and YAML files in a directory."""
    logging.info(f"Starting linting in directory: {data_dir}")
    data_path = Path(data_dir)
    if not data_path.is_dir():
        logging.error(f"Data directory not found: {data_dir}")
        return

    found_files = list(data_path.rglob("*.yaml")) + list(data_path.rglob("*.json"))

    for file_path in found_files:
        logging.info(f"Checking file: {file_path}")
        try:
            with open(file_path, 'r') as f:
                if file_path.suffix == '.json':
                    data = json.load(f)
                else:
                    data = yaml.safe_load(f)

            schema_name = data.get('$schema')
            if not schema_name:
                logging.warning(f"  -> SKIPPED: No '$schema' field found.")
                continue

            model = SCHEMA_REGISTRY.get(schema_name)
            if not model:
                logging.warning(f"  -> SKIPPED: No model found for schema '{schema_name}'.")
                continue

            model.model_validate(data)
            logging.info(f"  -> OK: Validated against '{schema_name}'.")

        except FileNotFoundError:
            logging.error(f"  -> ERROR: File not found during processing.")
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            logging.error(f"  -> ERROR: Could not parse file: {e}")
        except ValidationError as e:
            logging.error(f"  -> ERROR: Validation failed: {e}")
        except Exception as e:
            logging.error(f"  -> ERROR: An unexpected error occurred: {e}")


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
        lint_directory(args.data)
    elif args.command == "format":
        logging.info(f"Formatting file: {args.file}")
        # Future formatting functionality goes here

if __name__ == "__main__":
    main()
