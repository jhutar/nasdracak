import sys
import os
import pytest

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doit import lint_directory


def test_lint_directory():
    """Tests the lint_directory function."""
    test_dir = os.path.join(os.path.dirname(__file__), "test_lint_directory")
    issues = lint_directory(test_dir)

    # Expected issues
    expected_issues = {
        "ee-not-dict.yaml": [
            "File does not contain dictionary.",
        ],
        "ee-inalid-yaml.yaml": [
            "Could not parse file: while scanning a simple key",
        ],
        "ee-inalid-json.json": [
            "Could not parse file",
        ],
        "ee-missing-id.yaml": [
            "No 'id' field found.",
        ],
        "ee-unknown-id.yaml": [
            "No model found for schema 'MissingModel' (from id 'MissingModel:missing').",
        ],
        "ee-missing-property.yaml": [
            "Validation failed: 1 validation error for MeleeWeapon",
        ],
        "ee-extra-property.yaml": [
            "Validation failed: 1 validation error for MeleeWeapon",
        ],
        "ee-duplicate_b.yaml": [
            "Duplicate ID 'MeleeWeapon:ee-duplicate' found.",
        ],
        "ee-missing-in-inventory.yaml": [
            "Unknown inventory item 'CommonItem:magical-item-of-great-power' found.",
        ],
    }

    # Remove full paths
    issues_cleaned = {}
    for k, v in issues.items():
        k_base = os.path.basename(k)
        if k_base in (
            "ee-inalid-yaml.yaml",
            "ee-missing-property.yaml",
            "ee-extra-property.yaml",
        ):
            assert len(v) == 1
            v = [v[0].split("\n")[0]]
        if k_base == "ee-inalid-json.json":
            assert len(v) == 1
            v = [v[0].split(":")[0]]
        issues_cleaned[k_base] = v

    # Check that all expected files with issues are present
    assert issues_cleaned == expected_issues
