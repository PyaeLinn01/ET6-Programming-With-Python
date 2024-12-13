"""
test_mystery_2.py

This module contains unit tests for the `mystery_2` function in mystery_2.py.
"""

import unittest
from mystery_2 import mystery_2


class TestMystery2(unittest.TestCase):
    """Unit tests for the `mystery_2` function."""

    def test_non_empty_sequence(self):
        """Test non-empty sequences."""
        self.assertEqual(mystery_2([1, 2, 3]), 3)
        self.assertEqual(mystery_2("hello"), 5)
        self.assertEqual(mystery_2((1, 2)), 2)

    def test_empty_sequence(self):
        """Test empty sequences."""
        self.assertIsNone(mystery_2([]))
        self.assertIsNone(mystery_2(""))
        self.assertIsNone(mystery_2(()))

    def test_invalid_inputs(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            mystery_2(42)  # Not a sequence
        with self.assertRaises(TypeError):
            mystery_2(None)  # Not a sequence
        with self.assertRaises(TypeError):
            mystery_2(3.14)  # Not a sequence


if __name__ == "__main__":
    unittest.main()
