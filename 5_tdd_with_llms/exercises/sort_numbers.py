"""
sort_numbers.py

This module contains the `inclusive_or` function, which checks if a string
is present in at least one of two lists of strings.

Functions:
    inclusive_or(item, list1, list2): Returns True if `item` is in at least one of the lists.
"""

def sort_numbers(item, list1, list2):
    """
    Checks if an item is present in at least one of two lists.

    Args:
        item (str): The string to check for.
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        bool: True if `item` is in at least one of the lists, False otherwise.

    Raises:
        TypeError: If the inputs are of invalid types.
    """
    if not isinstance(item, str):
        raise TypeError("`item` must be a string.")
    if not isinstance(list1, list) or not all(isinstance(i, str) for i in list1):
        raise TypeError("`list1` must be a list of strings.")
    if not isinstance(list2, list) or not all(isinstance(i, str) for i in list2):
        raise TypeError("`list2` must be a list of strings.")

    return item in list1 or item in list2
