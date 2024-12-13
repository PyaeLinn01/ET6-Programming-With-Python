"""
mystery_1.py

This module contains the `mystery_1` function, which adds two input values together.

Functions:
    mystery_1(a, b): Adds two values and returns the result.
"""

def mystery_1(a, b):
    """
    Adds two input values and returns the result.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Returns:
        int or float: The sum of `a` and `b`.

    Raises:
        TypeError: If the inputs are not int or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b
