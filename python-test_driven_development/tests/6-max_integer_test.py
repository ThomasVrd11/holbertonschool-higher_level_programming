#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
""" Max integer - Unittest """


class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([3]), 3)

    def test_value(self):
        self.assertRaises(TypeError, max_integer, ['9', 5])

    def test_float(self):
        self.assertEqual(max_integer([2.4, 3]), 3)
