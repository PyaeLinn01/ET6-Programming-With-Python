"""
test_sort_numbers.py

This module contains unit tests for the `inclusive_or` function in inclusive_or.py.
"""

import unittest
from sort_numbers import inclusive_or


class TestInclusiveOr(unittest.TestCase):
    """Unit tests for the `inclusive_or` function."""

    def test_item_in_first_list(self):
        """Test when the item is in the first list."""
        self.assertTrue(inclusive_or("apple", ["apple", "banana"], ["orange", "grape"]))
        self.assertTrue(inclusive_or("cat", ["cat", "dog"], ["bird", "fish"]))

    def test_item_in_second_list(self):
        """Test when the item is in the second list."""
        self.assertTrue(inclusive_or("orange", ["apple", "banana"], ["orange", "grape"]))
        self.assertTrue(inclusive_or("fish", ["cat", "dog"], ["bird", "fish"]))

    def test_item_in_both_lists(self):
        """Test when the item is in both lists."""
        self.assertTrue(inclusive_or("apple", ["apple", "banana"], ["apple", "grape"]))

    def test_item_in_neither_list(self):
        """Test when the item is not in either list."""
        self.assertFalse(inclusive_or("kiwi", ["apple", "banana"], ["orange", "grape"]))
        self.assertFalse(inclusive_or("elephant", ["cat", "dog"], ["bird", "fish"]))

    def test_empty_lists(self):
        """Test with empty lists."""
        self.assertFalse(inclusive_or("apple", [], []))
        self.assertFalse(inclusive_or("cat", [], []))

    def test_invalid_item_input(self):
        """Test with invalid `item` input."""
        with self.assertRaises(TypeError):
            inclusive_or(123, ["apple", "banana"], ["orange", "grape"])
        with self.assertRaises(TypeError):
            inclusive_or(None, ["cat", "dog"], ["bird", "fish"])

    def test_invalid_list_input(self):
        """Test with invalid list inputs."""
        with self.assertRaises(TypeError):
            inclusive_or("apple", "not a list", ["orange", "grape"])
        with self.assertRaises(TypeError):
            inclusive_or("cat", ["cat", 123], ["bird", "fish"])
        with self.assertRaises(TypeError):
            inclusive_or("dog", ["cat", "dog"], "not a list")

if __name__ == "__main__":
    unittest.main()
