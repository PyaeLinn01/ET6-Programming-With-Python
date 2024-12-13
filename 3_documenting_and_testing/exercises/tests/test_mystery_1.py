"""
test_mystery_1.py

This module contains unit tests for the `mystery_1` function in mystery_1.py.
"""

import unittest
from mystery_1 import mystery_1


class TestMystery1(unittest.TestCase):
    """Unit tests for the `mystery_1` function."""

    def test_integers(self):
        """Test adding two integers."""
        self.assertEqual(mystery_1(2, 3), 5)
        self.assertEqual(mystery_1(-1, 1), 0)

    def test_floats(self):
        """Test adding two floating-point numbers."""
        self.assertAlmostEqual(mystery_1(1.1, 2.2), 3.3)

    def test_int_and_float(self):
        """Test adding an integer and a floating-point number."""
        self.assertAlmostEqual(mystery_1(1, 2.5), 3.5)

    def test_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(mystery_1(-2, -3), -5)

    def test_invalid_inputs(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            mystery_1("1", 2)
        with self.assertRaises(TypeError):
            mystery_1(1, "2")
        with self.assertRaises(TypeError):
            mystery_1("a", "b")


if __name__ == "__main__":
    unittest.main()
