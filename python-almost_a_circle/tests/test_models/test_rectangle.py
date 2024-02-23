#!/usr/bin/python3
"""Tests for the Rectancle class"""
import os
import json
import sys
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    """-------- BASECASES --------"""

    def test_rectangle_without_x_y(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_without_y(self):
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_without_id(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_all(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 5)

    """-------- TYPE ERROR --------"""

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    """-------- VALUE ERROR --------"""

    def test_value(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)

    """-------- METHODS --------"""

    def test_area(self):  # Test for area method
        rectangle = Rectangle(6, 2)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_str(self):  # Test for __str__ method
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_str = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(rectangle), expected_str)

    def test_display_without_x_y(self):  # Test for display method
        rectangle = Rectangle(2, 2)
        expected_output = "##\n##\n"
        old_stdout = sys.stdout
        # Redirect stdout temporarily to object StringIO
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout  # Put the orginal stdout back
        # Compare the output store in StringIO object with expected output
        self.assertEqual(mystdout.getvalue(), expected_output)

    def test_display_exist(self):
        rectangle = Rectangle(2, 4, 1, 2)
        expected_output = "\n\n ##\n ##\n ##\n ##\n"
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), expected_output)

    def test_update(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_to_dictionary(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_create(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle_dict = rectangle.to_dictionary()
        new_rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(str(rectangle), str(new_rectangle))

    def test_save_to_file_NONE(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle])
        new_rectangle = Rectangle.load_from_file()
        self.assertEqual(str(rectangle), str(new_rectangle[0]))
