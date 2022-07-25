#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case methods"""
    def test_integerlist(self):
        """Standard test with list of normal integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_emptylist(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 2, 4, 3], 4)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2]), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["Brie", "is", "my", "name"]), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
