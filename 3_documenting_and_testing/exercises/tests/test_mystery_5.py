"""
test_mystery_5.py

This module contains unit tests for the `mystery_5` function in mystery_5.py.
"""

import unittest
from mystery_5 import mystery_5


class TestMystery5(unittest.TestCase):
    """Unit tests for the `mystery_5` function."""

    def test_sort_and_append_to_new_list(self):
        """Test sorting and appending to a new list."""
        self.assertEqual(mystery_5([3, 1, 2]), [1, 2, 3])
        self.assertEqual(mystery_5([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort_and_append_to_existing_list(self):
        """Test sorting and appending to an existing list."""
        b = [10, 11]
        self.assertEqual(mystery_5([3, 1, 2], b), [10, 11, 1, 2, 3])

    def test_empty_list(self):
        """Test sorting an empty list."""
        self.assertEqual(mystery_5([]), [])

    def test_invalid_inputs(self):
        """Test invalid inputs."""
        with self.assertRaises(TypeError):
            mystery_5(123)  # Not a list
        with self.assertRaises(TypeError):
            mystery_5("abc")  # Not a list
        with self.assertRaises(TypeError):
            mystery_5([1, 2, 3], "not a list")  # Second argument not a list

    def test_mutation_of_original_list(self):
        """Ensure the original list `a` is modified and emptied."""
        a = [5, 3, 1]
        b = mystery_5(a)
        self.assertEqual(b, [1, 3, 5])
        self.assertEqual(a, [])  # `a` should be empty


if __name__ == "__main__":
    unittest.main()
