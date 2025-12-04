import sys
import os
import argparse
import tempfile
from pathlib import Path
import subprocess

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doit import expand_code_blocks   # noqa: E402


def test_expand_code_blocks():
    """Tests the expand_code_blocks function."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_dir = Path(tmpdirname)
        test_file = test_dir / "test.rst"
        original_content = "Header\n\n.. Vlozime seznam dovedností\n```echo -n Hello from test```\n\nFooter"
        with open(test_file, "w") as f:
            f.write(original_content)

        # Create a Namespace object to simulate argparse result
        args = argparse.Namespace(directory=str(test_dir))

        expand_code_blocks(args)

        with open(test_file, "r") as f:
            content = f.read()

        expected_content = "Header\n\n.. Vlozime seznam dovedností\nHello from test\n\nFooter"
        assert content == expected_content
