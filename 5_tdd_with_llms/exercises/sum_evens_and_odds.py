"""
sum_evens_and_odds.py

This module contains the `sum_evens_and_odds` function, which calculates 
the sum of even and odd numbers in a list.

Functions:
    sum_evens_and_odds(numbers): Returns a dictionary with sums of evens and odds.
"""

def sum_evens_and_odds(numbers):
    """
    Calculates the sum of even and odd numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        dict: A dictionary with keys "evens" and "odds", containing their respective sums.

    Raises:
        TypeError: If `numbers` is not a list of integers.
    """
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise TypeError("Input must be a list of integers.")
    
    evens = sum(n for n in numbers if n % 2 == 0)
    odds = sum(n for n in numbers if n % 2 != 0)
    
    return {"evens": evens, "odds": odds}
