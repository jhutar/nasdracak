import sys
import os
import pytest

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doit import split_string  # noqa: E402
from doit import format_price  # noqa: E402


@pytest.mark.parametrize(
    "text, max_length, expected",
    [
        ("Toto je testovaci text", 10, ["Toto je", "testovaci", "text"]),
        ("Toto je testovaci text", 20, ["Toto je testovaci", "text"]),
        ("Toto je testovaci text", 100, ["Toto je testovaci text"]),
        ("", 10, []),
        (" ", 10, []),
        ("slovo", 10, ["slovo"]),
        ("slovo abc", 5, ["slovo", "abc"]),
        ("dlouheslovo", 5, ["dlouh", "eslov", "o"]),
        ("Odstraňování pastí", 10, ["Odstraňová", "ní pastí"]),
        ("Moje odstraňování x", 10, ["Moje odstr", "aňování x"]),
        ("  extra   mezery  ", 10, ["extra", "mezery"]),
        (
            "Tohle je opravdu velmi dlouhý text, který se bude muset rozdělit na více řádků.",
            20,
            [
                "Tohle je opravdu",
                "velmi dlouhý text,",
                "který se bude muset",
                "rozdělit na více",
                "řádků.",
            ],
        ),
    ],
)
def test_split_string(text, max_length, expected):
    """Tests the split_string function."""
    assert split_string(text, max_length) == expected


@pytest.mark.parametrize(
    "price, expected",
    [
        (1.0, "1zl"),
        (1.1, "1zl 1st"),
        (1.11, "1zl 1st 1md"),
        (0.11, "1st 1md"),
        (0.01, "1md"),
        (0.099, "1st"),   # rounding anything below "md"
        (9.999, "10zl"),   # rounding anything below "md"
        (999.99, "999zl 9st 9md"),
        (1.01, "1zl 1md"),
    ],
)
def test_format_price(price, expected):
    """Test format_price function."""
    assert format_price(price) == expected
