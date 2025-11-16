
import sys
import os
import pytest

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from doit import lint_directory

def test_lint_directory():
    """Tests the lint_directory function."""
    test_dir = os.path.join(os.path.dirname(__file__), 'test_lint_directory')
    issues = lint_directory(test_dir)

    # Expected issues
    expected_issues = {
        'invalid_yaml.yaml': "Could not parse file: mapping values are not allowed here",
        'no_schema.yaml': "No '$schema' field found.",
        'unknown_schema.yaml': "No model found for schema 'UnknownSchema'.",
        'invalid_model.yaml': "Validation failed: 1 validation error for TestFile",
        'duplicate_name_2.yaml': "Duplicate name 'duplicate_name' found.",
    }

    # Check that all expected files with issues are present
    assert len(issues) == len(expected_issues)

    for file_path, file_issues in issues.items():
        file_name = os.path.basename(file_path)
        assert file_name in expected_issues
        # This is a simplification, we just check if the error message contains the expected string
        assert expected_issues[file_name] in file_issues[0]

    # valid_file.yaml and duplicate_name_1.yaml should not have issues
    # (duplicate_name_1 is processed before duplicate_name_2)
    assert not any('valid_file.yaml' in key for key in issues)
    assert not any('duplicate_name_1.yaml' in key for key in issues)
