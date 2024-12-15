"""
is_in_one.py

This module contains the `is_in_one` function, which checks if a string is present in only one of two lists.

Functions:
    is_in_one(item, list1, list2): Returns True if the item is in only one of the two lists, False otherwise.
"""

def is_in_one(item, list1, list2):
    """
    Checks if a string is present in only one of the given lists.

    Args:
        item (str): The string to check.
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        bool: True if the item is in only one of the lists, False otherwise.

    Raises:
        TypeError: If `list1` or `list2` are not lists or `item` is not a string.
    """
    if not isinstance(item, str):
        raise TypeError("`item` must be a string.")
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("`list1` and `list2` must be lists.")

    return (item in list1) != (item in list2)
