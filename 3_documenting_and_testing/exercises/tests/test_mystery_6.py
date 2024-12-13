"""
test_mystery_6.py

This module contains unit tests for the `mystery_6` function in mystery_6.py.
"""

import unittest
from mystery_6 import mystery_6


class TestMystery6(unittest.TestCase):
    """Unit tests for the `mystery_6` function."""

    def test_generate_list(self):
        """Test generating a list with valid inputs."""
        self.assertEqual(mystery_6(3, 5), [5, 6, 7], "Should generate a list of 3 integers starting from 5.")
        self.assertEqual(mystery_6(4, 0), [0, 1, 2, 3], "Should generate a list of 4 integers starting from 0.")

    def test_zero_length(self):
        """Test generating a list of length 0."""
        self.assertEqual(mystery_6(0, 10), [], "Should return an empty list.")

    def test_negative_length(self):
        """Test for negative `a` input."""
        with self.assertRaises(ValueError):
            mystery_6(-1, 5)

    def test_starting_from_negative(self):
        """Test starting from a negative integer."""
        self.assertEqual(mystery_6(3, -2), [-2, -1, 0], "Should handle negative starting points.")

    def test_single_element_list(self):
        """Test generating a list with one element."""
        self.assertEqual(mystery_6(1, 100), [100], "Should generate a list with one element.")

    def test_large_list(self):
        """Test generating a larger list."""
        result = mystery_6(1000, 0)
        self.assertEqual(len(result), 1000, "Should generate a list of 1000 integers.")
        self.assertEqual(result[:5], [0, 1, 2, 3, 4], "Should correctly generate the first 5 elements.")

if __name__ == "__main__":
    unittest.main()
