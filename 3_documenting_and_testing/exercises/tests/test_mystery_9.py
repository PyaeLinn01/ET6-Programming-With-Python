"""
test_mystery_9.py

This module contains unit tests for the `mystery_9` function in mystery_9.py.
"""

import unittest
from mystery_9 import mystery_9


class TestMystery9(unittest.TestCase):
    """Unit tests for the `mystery_9` function."""

    def test_valid_input(self):
        """Test valid inputs with numerical lists."""
        self.assertEqual(mystery_9([3, 2, 1]), [1, 2, 3], "Should sort the list in ascending order.")
        self.assertEqual(mystery_9([5, 4, 7, 1]), [1, 4, 5, 7], "Should sort the list in ascending order.")
        self.assertEqual(mystery_9([1, 2, 3]), [1, 2, 3], "Should return the list as it is already sorted.")
        self.assertEqual(mystery_9([]), [], "Should handle an empty list.")

    def test_with_negative_numbers(self):
        """Test lists containing negative numbers."""
        self.assertEqual(mystery_9([-3, -1, -2, 0]), [-3, -2, -1, 0], "Should correctly sort negative numbers.")

    def test_with_duplicates(self):
        """Test lists containing duplicate values."""
        self.assertEqual(mystery_9([3, 1, 2, 1]), [1, 1, 2, 3], "Should correctly sort a list with duplicates.")

    def test_invalid_inputs(self):
        """Test invalid input types."""
        with self.assertRaises(TypeError):
            mystery_9("not_a_list")
        with self.assertRaises(TypeError):
            mystery_9([1, 2, "three"])

    def test_single_element(self):
        """Test lists with a single element."""
        self.assertEqual(mystery_9([42]), [42], "Should handle a list with a single element.")

if __name__ == "__main__":
    unittest.main()
