"""
mystery_2.py

This module contains the `mystery_2` function, which checks the length of a given sequence.

Functions:
    mystery_2(a): Returns the length of the input sequence or None if it's empty.
"""

def mystery_2(a):
    """
    Returns the length of the input sequence or None if it is empty.

    Args:
        a (sequence): The input sequence (e.g., string, list, tuple).

    Returns:
        int: The length of the sequence if it is not empty.
        None: If the sequence is empty.

    Raises:
        TypeError: If the input is not a sequence (e.g., not iterable).
    """
    if not hasattr(a, "__len__"):
        raise TypeError("Input must be a sequence (e.g., string, list, tuple).")

    if len(a) == 0:
        return None

    return len(a)
