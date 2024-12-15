"""
is_in_both.py

This module contains the `is_in_both` function, which checks if a string is present in two lists.

Functions:
    is_in_both(item, list1, list2): Returns True if the item is in both lists, False otherwise.
"""

def is_in_both(item, list1, list2):
    """
    Checks if a string is present in both of the given lists.

    Args:
        item (str): The string to check.
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        bool: True if the item is in both lists, False otherwise.

    Raises:
        TypeError: If `list1` or `list2` are not lists or `item` is not a string.
    """
    if not isinstance(item, str):
        raise TypeError("`item` must be a string.")
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("`list1` and `list2` must be lists.")

    return item in list1 and item in list2
