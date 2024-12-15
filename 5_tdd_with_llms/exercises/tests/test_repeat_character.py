"""
test_repeat_character.py

This module contains unit tests for the `repeat_character` function in repeat_character.py.
"""

import unittest
from repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Unit tests for the `repeat_character` function."""

    def test_repeat_single_occurrence(self):
        """Test repeating a character that occurs once."""
        self.assertEqual(repeat_character("apple", "p", 3), "apppppple")
        self.assertEqual(repeat_character("hello", "h", 2), "hhello")

    def test_repeat_multiple_occurrences(self):
        """Test repeating a character that occurs multiple times."""
        self.assertEqual(repeat_character("banana", "a", 2), "baanaanaa")
        self.assertEqual(repeat_character("mississippi", "s", 4), "miissssssissssssippi")

    def test_no_occurrences(self):
        """Test when the character does not exist in the string."""
        self.assertEqual(repeat_character("orange", "z", 3), "orange")
        self.assertEqual(repeat_character("cat", "x", 1), "cat")

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(repeat_character("", "a", 3), "")

    def test_zero_repetitions(self):
        """Test when the number of repetitions is zero."""
        self.assertEqual(repeat_character("hello", "l", 0), "heo")
        self.assertEqual(repeat_character("world", "o", 0), "wrld")

    def test_invalid_char_input(self):
        """Test with invalid `char` input."""
        with self.assertRaises(ValueError):
            repeat_character("hello", "ll", 3)
        with self.assertRaises(ValueError):
            repeat_character("hello", "", 2)

    def test_negative_repetitions(self):
        """Test when `n` is negative."""
        with self.assertRaises(ValueError):
            repeat_character("hello", "l", -2)

    def test_invalid_input_types(self):
        """Test with invalid input types."""
        with self.assertRaises(TypeError):
            repeat_character(123, "a", 2)
        with self.assertRaises(TypeError):
            repeat_character("hello", 1, 2)
        with self.assertRaises(ValueError):
            repeat_character("hello", "l", "three")

if __name__ == "__main__":
    unittest.main()
