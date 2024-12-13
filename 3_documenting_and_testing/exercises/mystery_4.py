"""
mystery_4.py

This module contains the `mystery_4` function, which generates a list of sequential integers.

Functions:
    mystery_4(a): Returns a list of the first `a` non-negative integers.
"""

def mystery_4(a):
    """
    Generates a list of the first `a` non-negative integers.

    Args:
        a (int): The number of integers to generate.

    Returns:
        list: A list containing the first `a` non-negative integers.

    Raises:
        ValueError: If `a` is negative.
        TypeError: If `a` is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError("Input must be an integer")
    if a < 0:
        raise ValueError("Input must be a non-negative integer")

    b = []
    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
