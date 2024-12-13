"""
test_mystery_8.py

This module contains unit tests for the `mystery_8` function in mystery_8.py.
"""

import unittest
from mystery_8 import mystery_8


class TestMystery8(unittest.TestCase):
    """Unit tests for the `mystery_8` function."""

    def test_valid_input(self):
        """Test valid inputs with a mix of matching and non-matching strings."""
        self.assertEqual(mystery_8(["apple", "banana", "cherry"], "a"), ["apple", "banana"], "Should return strings containing 'a'.")
        self.assertEqual(mystery_8(["cat", "dog", "bird"], "cat"), ["cat"], "Should return ['cat'] as it contains 'cat'.")
        self.assertEqual(mystery_8(["one", "two", "three"], "four"), [], "Should return an empty list as 'four' is not in any string.")

    def test_empty_list(self):
        """Test when the input list is empty."""
        self.assertEqual(mystery_8([], "a"), [], "Should return an empty list when input is empty.")

    def test_empty_substring(self):
        """Test when the substring is empty."""
        self.assertEqual(mystery_8(["alpha", "beta", "gamma"], ""), ["alpha", "beta", "gamma"], "Should return all strings for an empty substring.")

    def test_case_sensitivity(self):
        """Test for case sensitivity."""
        self.assertEqual(mystery_8(["Cat", "dog", "bird"], "cat"), [], "Should return an empty list as the search is case-sensitive.")
        self.assertEqual(mystery_8(["Cat", "dog", "bird"], "Cat"), ["Cat"], "Should match 'Cat' exactly.")

    def test_invalid_inputs(self):
        """Test for invalid input types."""
        with self.assertRaises(TypeError):
            mystery_8("not_a_list", "a")
        with self.assertRaises(TypeError):
            mystery_8(["valid", "list"], 123)

    def test_substring_at_edges(self):
        """Test substrings at the edges of strings."""
        self.assertEqual(mystery_8(["start", "middle", "end"], "end"), ["end"], "Should match the substring at the end of a string.")
        self.assertEqual(mystery_8(["start", "middle", "end"], "sta"), ["start"], "Should match the substring at the start of a string.")

if __name__ == "__main__":
    unittest.main()
