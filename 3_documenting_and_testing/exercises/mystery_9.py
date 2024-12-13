"""
mystery_9.py

This module contains the `mystery_9` function, which performs a bubble sort on a list.

Functions:
    mystery_9(a): Sorts a list in ascending order using the bubble sort algorithm.
"""

def mystery_9(a):
    """
    Sorts a list of comparable elements in ascending order using the bubble sort algorithm.

    Args:
        a (list): A list of elements to sort. All elements must be comparable.

    Returns:
        list: The sorted list in ascending order.

    Raises:
        TypeError: If `a` is not a list or if its elements are not comparable.
    """
    if not isinstance(a, list):
        raise TypeError("`a` must be a list.")
    if not all(isinstance(x, (int, float)) for x in a):
        raise TypeError("`a` must contain only numbers.")

    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
