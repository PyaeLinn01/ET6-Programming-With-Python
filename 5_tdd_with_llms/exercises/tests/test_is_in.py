"""
test_is_in.py

This module contains unit tests for the `is_in` function in is_in.py.
"""

import unittest
from is_in import is_in


class TestIsIn(unittest.TestCase):
    """Unit tests for the `is_in` function."""

    def test_item_in_one_list(self):
        """Test when the item is present in only one list."""
        self.assertTrue(is_in("apple", ["apple", "banana"], ["cherry", "grape"]))
        self.assertTrue(is_in("cat", ["dog", "cat"], ["mouse", "lion"]))

    def test_item_in_both_lists(self):
        """Test when the item is present in both lists."""
        self.assertTrue(is_in("apple", ["apple", "banana"], ["apple", "cherry"]))
        self.assertTrue(is_in("cat", ["dog", "cat"], ["cat", "mouse"]))

    def test_item_in_neither_list(self):
        """Test when the item is not present in either list."""
        self.assertFalse(is_in("apple", ["banana", "cherry"], ["grape", "orange"]))

    def test_empty_lists(self):
        """Test when one or both lists are empty."""
        self.assertFalse(is_in("apple", [], []))
        self.assertTrue(is_in("cat", ["dog", "rabbit"], []))
        self.assertTrue(is_in("mouse", [], ["lion", "tiger"]))

    def test_invalid_inputs(self):
        """Test invalid input types."""
        with self.assertRaises(TypeError):
            is_in(123, ["123"], ["123"])
        with self.assertRaises(TypeError):
            is_in("apple", "not_a_list", ["apple"])
        with self.assertRaises(TypeError):
            is_in("apple", ["apple"], "not_a_list")

    def test_case_sensitivity(self):
        """Test case sensitivity of the string comparison."""
        self.assertFalse(is_in("Apple", ["apple"], ["pear"]))
        self.assertTrue(is_in("apple", ["apple"], ["pear"]))

if __name__ == "__main__":
    unittest.main()
