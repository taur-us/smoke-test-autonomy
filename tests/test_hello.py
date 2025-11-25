"""Tests for the hello module."""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hello import greet


def test_greet_no_args():
    """Test greet() returns 'Hello, World!' when called without arguments."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_with_name():
    """Test greet('Claude') returns 'Hello, Claude!'."""
    result = greet("Claude")
    assert result == "Hello, Claude!"


def test_greet_with_different_name():
    """Test greet() works with different names."""
    result = greet("Alice")
    assert result == "Hello, Alice!"


def test_greet_with_empty_string():
    """Test greet('') returns 'Hello, !' for empty string."""
    result = greet("")
    assert result == "Hello, !"


if __name__ == "__main__":
    test_greet_no_args()
    test_greet_with_name()
    test_greet_with_different_name()
    test_greet_with_empty_string()
    print("All tests passed!")
