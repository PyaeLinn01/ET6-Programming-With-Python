"""
mystery_8.py

This module contains the `mystery_8` function, which filters a list of strings
to include only those containing a specific substring.

Functions:
    mystery_8(a, b): Filters strings containing a given substring using a while loop.
"""

def mystery_8(a, b):
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
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]  # Reduce the list by removing the first element
    return c
