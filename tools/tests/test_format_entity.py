import sys
import os
import argparse
from pathlib import Path

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doit import format_entity  # noqa: E402


def test_format_entity_single_entity(tmp_path):
    """Tests the format_entity function for a single entity using static data."""
    test_data_dir = Path("tools/tests/test_format_entity/data")
    template_file = Path("tools/tests/test_format_entity/templates/single_weapon.yaml.j2")
    output_dir = tmp_path

    args = argparse.Namespace(
        data=str(test_data_dir),
        entity="MeleeWeapon:mec-rezavy",
        model=None,
        template=str(template_file),
        output_dir=str(output_dir),
        all_in_one=False,
    )

    format_entity(args)

    expected_output_file = output_dir / "Meč po dědovi.yaml"
    assert expected_output_file.exists()
    output_content = expected_output_file.read_text()
    expected_content = """
Name: Meč po dědovi
Description: Rezavý meč.
Demage: 1
"""
    assert output_content.strip() == expected_content.strip()


def test_format_entity_all_in_one(tmp_path):
    """Tests the format_entity function with --all-in-one option using static data."""
    test_data_dir = Path("tools/tests/test_format_entity/data")
    template_file = Path("tools/tests/test_format_entity/templates/all_weapons.yaml.j2")
    output_dir = tmp_path

    args = argparse.Namespace(
        data=str(test_data_dir),
        entity=None,
        model="MeleeWeapon",
        template=str(template_file),
        output_dir=str(output_dir),
        all_in_one=True,
    )

    format_entity(args)

    expected_output_file = output_dir / "all.yaml"
    assert expected_output_file.exists()
    output_content = expected_output_file.read_text().strip()

    expected_content = """
Name: Meč po dědovi
Demage: 1
---

Name: Sekera válečná
Demage: 2
---
"""
    # Normalize by sorting lines to avoid issues with entity order
    assert sorted(output_content.splitlines()) == sorted(expected_content.strip().splitlines())
