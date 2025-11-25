#!/usr/bin/env python3
"""
Tests for hello.py greet() function.

This module provides pytest tests to verify the greet() function
meets its acceptance criteria:
- Returns 'Hello, World!' when called without arguments
- Returns 'Hello, {name}!' when called with a name parameter
"""

import pytest

from hello import greet


class TestGreet:
    """Test suite for the greet() function."""

    def test_greet_default(self):
        """Test greet() returns default greeting when called without arguments.

        Acceptance Criterion: greet() function returns 'Hello, World!'
        when called without arguments.
        """
        result = greet()
        expected = 'Hello, World!'
        assert result == expected, f"Expected '{expected}', got '{result}'"

    def test_greet_with_name(self):
        """Test greet() returns personalized greeting with name argument.

        Acceptance Criterion: greet('Claude') returns 'Hello, Claude!'
        """
        result = greet('Claude')
        expected = 'Hello, Claude!'
        assert result == expected, f"Expected '{expected}', got '{result}'"

    @pytest.mark.parametrize("name,expected", [
        ('Alice', 'Hello, Alice!'),
        ('Bob', 'Hello, Bob!'),
        ('World', 'Hello, World!'),
        ('123', 'Hello, 123!'),
    ])
    def test_greet_with_different_names(self, name, expected):
        """Test greet() handles various name inputs correctly.

        This parametrized test ensures the function works with
        different types of name inputs.
        """
        result = greet(name)
        assert result == expected, f"Expected '{expected}', got '{result}'"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
