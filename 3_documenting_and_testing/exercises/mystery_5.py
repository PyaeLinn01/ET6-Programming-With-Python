"""
mystery_5.py

This module contains the `mystery_5` function, which sorts elements in a list and appends them to another list.

Functions:
    mystery_5(a, b=None): Sorts elements from list `a` into list `b`.
"""

def mystery_5(a, b=None):
    """
    Sorts the elements of list `a` in ascending order and appends them to list `b`.

    If `b` is not provided, a new list is created.

    Args:
        a (list): The list of elements to sort and remove. Elements must be comparable.
        b (list, optional): The list to which sorted elements are appended. Defaults to an empty list.

    Returns:
        list: The list `b` containing elements of `a` in ascending order.

    Raises:
        TypeError: If `a` is not a list or `b` is not a list.
    """
    if not isinstance(a, list) or (b is not None and not isinstance(b, list)):
        raise TypeError("Both `a` and `b` must be lists.")

    if b is None:
        b = []

    while a:
        c = min(a)
        a.remove(c)
        b.append(c)

    return b
