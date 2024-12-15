"""
repeat_character.py

This module contains the `repeat_character` function, which repeats each occurrence
of a specific character in a string a specified number of times.

Functions:
    repeat_character(text, char, n): Repeats occurrences of a character in a string.
"""

def repeat_character(text, char, n):
    """
    Repeats each occurrence of a specified character in a string `n` times.

    Args:
        text (str): The input string.
        char (str): The character to repeat.
        n (int): The number of times to repeat the character.

    Returns:
        str: A new string with each occurrence of `char` repeated `n` times.

    Raises:
        ValueError: If `char` is not a single character or `n` is negative.
        TypeError: If inputs are of invalid types.
    """
    if not isinstance(text, str):
        raise TypeError("`text` must be a string.")
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("`char` must be a single character string.")
    if not isinstance(n, int) or n < 0:
        raise ValueError("`n` must be a non-negative integer.")

    result = ""
    for c in text:
        if c == char:
            result += c * n
        else:
            result += c
    return result
