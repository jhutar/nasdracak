
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
        'no_schema.yaml': "File is empty or contains only comments.",
        'unknown_schema.yaml': "No model found for schema 'UnknownSchema' (from id 'UnknownSchema:unknown_schema_test').",
        'invalid_model.yaml': "Validation failed: 1 validation error for TestFile",
    }
    # Check that all expected files with issues are present
    assert len(issues) == len(expected_issues) + 1 # +1 for the duplicate ID file

    found_duplicate_id_issue = False
    for file_path, file_issues in issues.items():
        file_name = os.path.basename(file_path)
        if file_name in expected_issues:
            assert expected_issues[file_name] in file_issues[0]
        elif file_name in ['duplicate_name_1.yaml', 'duplicate_name_2.yaml']:
            if "Duplicate ID 'TestFile:duplicate_id' found." in file_issues[0]:
                found_duplicate_id_issue = True
        else:
            pytest.fail(f"Unexpected file with issues: {file_name}")
    assert found_duplicate_id_issue, "Expected a duplicate ID issue, but none was found."

    # valid_file.yaml should not have issues
    assert not any(os.path.basename(key) == 'valid_file.yaml' for key in issues)
