"""
test_is_in_both.py

This module contains unit tests for the `is_in_both` function in is_in_both.py.
"""

import unittest
from is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Unit tests for the `is_in_both` function."""

    def test_item_in_both(self):
        """Test when the item is present in both lists."""
        self.assertTrue(is_in_both("apple", ["apple", "banana"], ["apple", "cherry"]))
        self.assertTrue(is_in_both("cat", ["dog", "cat"], ["cat", "mouse"]))

    def test_item_not_in_both(self):
        """Test when the item is not present in both lists."""
        self.assertFalse(is_in_both("apple", ["apple", "banana"], ["cherry", "grape"]))
        self.assertFalse(is_in_both("cat", ["dog", "rabbit"], ["mouse", "lion"]))

    def test_item_not_in_either(self):
        """Test when the item is not in either list."""
        self.assertFalse(is_in_both("apple", ["banana", "cherry"], ["grape", "orange"]))

    def test_empty_lists(self):
        """Test when one or both lists are empty."""
        self.assertFalse(is_in_both("apple", [], []))
        self.assertFalse(is_in_both("cat", ["dog", "rabbit"], []))
        self.assertFalse(is_in_both("mouse", [], ["lion", "tiger"]))

    def test_invalid_inputs(self):
        """Test invalid input types."""
        with self.assertRaises(TypeError):
            is_in_both(123, ["123"], ["123"])
        with self.assertRaises(TypeError):
            is_in_both("apple", "not_a_list", ["apple"])
        with self.assertRaises(TypeError):
            is_in_both("apple", ["apple"], "not_a_list")

    def test_case_sensitivity(self):
        """Test case sensitivity of the string comparison."""
        self.assertFalse(is_in_both("Apple", ["apple"], ["apple"]))
        self.assertTrue(is_in_both("apple", ["apple"], ["apple"]))

if __name__ == "__main__":
    unittest.main()
