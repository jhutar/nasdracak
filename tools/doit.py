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
import random
import jinja2
import os

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

    for file_path in models.list_dir_files(data_path):
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

        # Check modifiers only point at existing items
        if hasattr(item, "modifiers"):
            for mod_id, mod_val in item.modifiers.items():
                if mod_id not in seen_ids:
                    issue = f"Unknown modifier '{mod_id}' found."
                    logging.warning(f"  -> ERROR: {issue}")
                    issues[str(item._file_path)].append(issue)
                if mod_val < 0:
                    issue = f"Negative value for modifier '{mod_id}' found."
                    logging.warning(f"  -> ERROR: {issue}")
                    issues[str(item._file_path)].append(issue)
                if mod_val == 1:
                    issue = f"Value 1 does not make sense for modifier '{mod_id}' (anything * 1 does not change anything)."
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


def split_string(text: str, max_length: int) -> typing.List[str]:
    """Splits a string into a list of strings, with a maximum length for each string, without splitting words."""
    words = text.split()

    lines = []
    current_line = ""
    for word in words:
        # Skip processing empty words
        if len(word) == 0:
            continue
        # If a word is longer than max_length, we have to split it
        elif len(word) > max_length:
            if len(current_line) == 0:
                chunk = word[:max_length]
                current_line = chunk
            else:
                chunk = word[:max_length - len(current_line) - 1]
                current_line += " " + chunk
            lines.append(current_line)
            current_line = ""
            word = word[len(chunk):]
            for i in range(0, len(word), max_length):
                current_line = word[i:i+max_length]
                if len(current_line) >= max_length:
                    lines.append(current_line)
                    current_line = ""
        # If we would overflow max_length with current word
        elif len(current_line) + len(word) + 1 > max_length:
            lines.append(current_line)
            current_line = word
        # If this is first word on the line, do not start with space
        elif len(current_line) == 0:
            current_line = word
        # This is just a word that can be added to current line
        else:
            current_line += " " + word

    if current_line:
        lines.append(current_line)

    return lines


def format_entity(args: argparse.Namespace):
    world = models.World(pathlib.Path(args.data))
    if args.entity:
        entities = [world.get_by_id(args.entity)]
    elif args.model:
        entities = world.get_by_model(args.model)
    else:
        raise Exception("Neither entity ID or model provided.")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(args.template)),
        autoescape=jinja2.select_autoescape(["html", "xml", "md", "svg"]),
    )
    env.filters["split_string"] = split_string
    template_name = os.path.basename(args.template)
    template = env.get_template(template_name)

    for e in entities:
        e_rendered = template.render({"entity": e})
        if args.output_dir:
            tmp = template_name
            if tmp.endswith(".j2"):
                tmp = tmp.replace(".j2", "")
            tmp = tmp.split(".")[-1]
            file_name = e.name + "." + tmp
            file_path = os.path.join(args.output_dir, file_name)
            with open(file_path, "w") as fd:
                fd.write(e_rendered)
        else:
            print(e_rendered)

def generate_character(args: argparse.Namespace):
    world = models.World(pathlib.Path(args.data))

    def pick_one(provided: str, model: models.BaseModelWithId) -> models.BaseModelWithId:
        if provided:
            out = world.get(model, provided)
        else:
            out = world.pick(model)
        if hasattr(out, "modifiers"):
            world.update_probabilities(out.modifiers)
        print(f"{out.__class__.__name__}: {out.name}")
        return out

    # Level
    _level = args.level; print(f"Level: {_level}")

    # Race
    _race = pick_one(args.race, models.Race)

    # Name
    if args.name:
        _name = args.name
    else:
        _name = random.choice(_race.names); print(f"Name: {_name}")

    # Appearance
    _appearance = ""

    # Background
    _background = ""

    # Location
    _location = pick_one(args.location, models.Location)

    # Occupation
    _occupation = pick_one(args.occupation, models.Occupation)

    # Inventory
    _inventory = []

    # Stats
    _properties = [world.pick(models.Property) for i in range(3)]
    _strength = _race.innate_strength + len([i for i in _properties if i.id == "Property:sila"])
    _dexterity = _race.innate_dexterity + len([i for i in _properties if i.id == "Property:obratnost"])
    _inteligence = _race.innate_inteligence + len([i for i in _properties if i.id == "Property:inteligence"])
    _charisma = _race.innate_charisma + len([i for i in _properties if i.id == "Property:charisma"])
    print(f"props: {', '.join([i.id for i in _properties])}")
    print(f"SÍL/OBR/INT/CHAR: {_strength}/{_dexterity}/{_inteligence}/{_charisma}")

    # Health and magenergy
    _health = 5 + _strength + _dexterity if _strength + _dexterity > 0 else 5
    _magenergy = 5 + _inteligence + _charisma if _inteligence + _charisma > 0 else 5
    print(f"Health & Magenergy: {_health} & {_magenergy}")


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
    format_parser.add_argument("--entity", help="Display one specific entity ID.")
    format_parser.add_argument("--model", help="Display all entities with given model.")
    format_parser.add_argument("--template", required=True, help="Jinja2 template for rendering.")
    format_parser.add_argument("--output-dir", help="Dump output file(s) to this directory.")

    # Generate character command
    character_parser = subparsers.add_parser("character", help="Generate a character.", description="If no choice is specified, it will be picked randomly.")
    character_parser.add_argument("--level", help="What is the level of the character.", default=1, type=int)
    character_parser.add_argument("--race", help="Race and sex of the character.")
    character_parser.add_argument("--name", help="Name of the character.")
    character_parser.add_argument("--location", help="Where does the character live.")
    character_parser.add_argument("--occupation", help="What does the character do for living.")

    args = parser.parse_args()
    setup_logging(args)

    logging.debug(f"Using data directory: {args.data}")

    if args.command == "lint":
        if lint_directory(args.data):
            sys.exit(1)
    elif args.command == "format":
        if format_entity(args):
            sys.exit(1)
    elif args.command == "character":
        if generate_character(args):
            sys.exit(1)


if __name__ == "__main__":
    main()
