"""
mystery_7.py

This module contains the `mystery_7` function, which filters a list of strings
to include only those containing a specific substring.

Functions:
    mystery_7(a, b): Filters strings containing a given substring.
"""

def mystery_7(a, b):
    """
    Filters a list of strings, returning only those that contain the substring `b`.

    Args:
        a (list of str): A list of strings to search.
        b (str): The substring to search for.

    Returns:
        list of str: A list of strings from `a` that contain the substring `b`.

    Raises:
        TypeError: If `a` is not a list of strings or `b` is not a string.
    """
    if not isinstance(a, list) or not all(isinstance(item, str) for item in a):
        raise TypeError("`a` must be a list of strings.")
    if not isinstance(b, str):
        raise TypeError("`b` must be a string.")

    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
