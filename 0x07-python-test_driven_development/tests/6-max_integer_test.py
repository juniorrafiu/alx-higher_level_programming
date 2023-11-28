#!/usr/bin/python3
""" unittest max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    def test_beginning(self):
        """Test for max at the beginning of list"""
        max = [30, 2, 4, 5, 9]
        self.assertEqual(max_integer(max), 30)

    def test_end(self):
        """Test for max at the ending of list"""
        max = [30, 2, 4, 5, 90]
        self.assertEqual(max_integer(max), 90)

    def test_middle(self):
        """Test for max at the middle of list"""
        max = [30, 2, 40, 5, 9]
        self.assertEqual(max_integer(max), 40)

    def test_one_element(self):
        """Test for max at the beginning of list"""
        max = [30]
        self.assertEqual(max_integer(max), 30)

    def test_empty(self):
        """Test for max at the beginning of list"""
        max = []
        self.assertIsNone(max_integer(max))

    def test_negatives(self):
        """Test for max at the beginning of list"""
        max = [-30, -2, -4, -5, -9]
        self.assertEqual(max_integer(max), -2)

    def test_one_negative(self):
        """Test for max at the beginning of list"""
        max = [-30, 2, 4, 5, 9]
        self.assertEqual(max_integer(max), 9)


if __name__ == "__main__":
    unittest.main()
