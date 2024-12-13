"""
test_mystery_3.py

This module contains unit tests for the `mystery_3` function in mystery_3.py.
"""

import unittest
from mystery_3 import mystery_3


class TestMystery3(unittest.TestCase):
    """Unit tests for the `mystery_3` function."""

    def test_a_less_than_b(self):
        """Test cases where a < b."""
        self.assertEqual(mystery_3(3, 5), 3)
        self.assertEqual(mystery_3(-2, 2), -2)

    def test_a_greater_than_b(self):
        """Test cases where a > b."""
        self.assertEqual(mystery_3(7, 4), 4)
        self.assertEqual(mystery_3(0, -1), -1)

    def test_a_equals_b(self):
        """Test cases where a == b."""
        self.assertEqual(mystery_3(3, 3), 6)
        self.assertEqual(mystery_3(0, 0), 0)
        self.assertEqual(mystery_3(-5, -5), -10)

    def test_invalid_inputs(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            mystery_3("3", 3)
        with self.assertRaises(TypeError):
            mystery_3(3, "3")
        with self.assertRaises(TypeError):
            mystery_3("a", "b")


if __name__ == "__main__":
    unittest.main()
