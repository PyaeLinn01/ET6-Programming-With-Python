"""
mystery_3.py

This module contains the `mystery_3` function, which performs conditional logic on two input values.

Functions:
    mystery_3(a, b): Returns the smaller value, or their sum if they are equal.
"""

def mystery_3(a, b):
    """
    Returns the smaller of the two inputs. If the inputs are equal, returns their sum.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Returns:
        int or float: The smaller value, or the sum if `a` equals `b`.

    Raises:
        TypeError: If the inputs are not int or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
