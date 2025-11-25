#!/usr/bin/env python3
"""
Hello module with greet function.

This module provides a simple greeting function that returns
personalized greeting messages.
"""


def greet(name: str = None) -> str:
    """
    Return a greeting message.

    Args:
        name: Optional name to include in greeting.
              If None, returns default greeting.

    Returns:
        str: Greeting message in format 'Hello, World!' or 'Hello, {name}!'
    """
    if name is None:
        return 'Hello, World!'
    return f'Hello, {name}!'


if __name__ == '__main__':
    print(greet())
    print(greet('Claude'))
