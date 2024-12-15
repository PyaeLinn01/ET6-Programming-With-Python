
"""
test_sum_evens_and_odds.py

This module contains unit tests for the `sum_evens_and_odds` function in sum_evens_and_odds.py.
"""

import unittest
from sum_evens_and_odds import sum_evens_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    """Unit tests for the `sum_evens_and_odds` function."""

    def test_all_evens(self):
        """Test a list with only even numbers."""
        self.assertEqual(sum_evens_and_odds([2, 4, 6, 8]), {"evens": 20, "odds": 0})

    def test_all_odds(self):
        """Test a list with only odd numbers."""
        self.assertEqual(sum_evens_and_odds([1, 3, 5, 7]), {"evens": 0, "odds": 16})

    def test_mixed_numbers(self):
        """Test a list with both even and odd numbers."""
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4]), {"evens": 6, "odds": 4})

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(sum_evens_and_odds([]), {"evens": 0, "odds": 0})

    def test_single_even(self):
        """Test a list with a single even number."""
        self.assertEqual(sum_evens_and_odds([2]), {"evens": 2, "odds": 0})

    def test_single_odd(self):
        """Test a list with a single odd number."""
        self.assertEqual(sum_evens_and_odds([3]), {"evens": 0, "odds": 3})

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(sum_evens_and_odds([-1, -2, -3, -4]), {"evens": -6, "odds": -4})

    def test_invalid_input(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            sum_evens_and_odds("not a list")
        with self.assertRaises(TypeError):
            sum_evens_and_odds([1, 2, "three", 4])

if __name__ == "__main__":
    unittest.main()
