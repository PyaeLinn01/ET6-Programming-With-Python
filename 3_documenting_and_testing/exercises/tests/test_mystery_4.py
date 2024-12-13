"""
test_mystery_4.py

This module contains unit tests for the `mystery_4` function in mystery_4.py.
"""

import unittest
from mystery_4 import mystery_4


class TestMystery4(unittest.TestCase):
    """Unit tests for the `mystery_4` function."""

    def test_valid_input(self):
        """Test valid input values."""
        self.assertEqual(mystery_4(0), [])
        self.assertEqual(mystery_4(1), [0])
        self.assertEqual(mystery_4(5), [0, 1, 2, 3, 4])

    def test_large_input(self):
        """Test larger input values."""
        self.assertEqual(mystery_4(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_invalid_inputs(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            mystery_4("5")  # String instead of integer
        with self.assertRaises(TypeError):
            mystery_4(5.5)  # Float instead of integer

    def test_negative_input(self):
        """Test negative input."""
        with self.assertRaises(ValueError):
            mystery_4(-1)


if __name__ == "__main__":
    unittest.main()
