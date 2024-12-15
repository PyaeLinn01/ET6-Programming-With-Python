
"""
test_is_in_one.py

This module contains unit tests for the `is_in_one` function in is_in_one.py.
"""

import unittest
from is_in_one import is_in_one


class TestIsInOne(unittest.TestCase):
    """Unit tests for the `is_in_one` function."""

    def test_item_in_only_one_list(self):
        """Test when the item is present in only one list."""
        self.assertTrue(is_in_one("apple", ["apple", "banana"], ["cherry", "grape"]))
        self.assertTrue(is_in_one("cat", ["dog", "cat"], ["mouse", "lion"]))

    def test_item_in_both_lists(self):
        """Test when the item is present in both lists."""
        self.assertFalse(is_in_one("apple", ["apple", "banana"], ["apple", "cherry"]))
        self.assertFalse(is_in_one("cat", ["dog", "cat"], ["cat", "mouse"]))

    def test_item_in_neither_list(self):
        """Test when the item is not present in either list."""
        self.assertFalse(is_in_one("apple", ["banana", "cherry"], ["grape", "orange"]))

    def test_empty_lists(self):
        """Test when one or both lists are empty."""
        self.assertFalse(is_in_one("apple", [], []))
        self.assertTrue(is_in_one("cat", ["dog", "rabbit"], []))
        self.assertTrue(is_in_one("mouse", [], ["lion", "tiger"]))

    def test_invalid_inputs(self):
        """Test invalid input types."""
        with self.assertRaises(TypeError):
            is_in_one(123, ["123"], ["123"])
        with self.assertRaises(TypeError):
            is_in_one("apple", "not_a_list", ["apple"])
        with self.assertRaises(TypeError):
            is_in_one("apple", ["apple"], "not_a_list")

    def test_case_sensitivity(self):
        """Test case sensitivity of the string comparison."""
        self.assertTrue(is_in_one("Apple", ["apple"], ["Apple"]))
        self.assertFalse(is_in_one("apple", ["apple"], ["apple"]))

if __name__ == "__main__":
    unittest.main()
