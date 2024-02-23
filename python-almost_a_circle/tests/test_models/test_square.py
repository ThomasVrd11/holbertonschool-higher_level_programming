#!/usr/bin/python3
"""Tests for the Square class"""
import os
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    """-------- BASECASES --------"""

    def test_Square_without_x_y(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_Square_without_y(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_without_id(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_with_all(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    """-------- TYPE ERROR --------"""

    def test_Square_size_type(self):
        with self.assertRaises(TypeError):
            square = Square("1")

    def test_Square_x_type(self):
        with self.assertRaises(TypeError):
            square = Square(1, "2")

    def test_Square_y_type(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, "3")

    """-------- VALUE ERROR --------"""

    def test_Square_size_value(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_Square_x_value(self):
        with self.assertRaises(ValueError):
            square = Square(1, -2)

    def test_Square_y_value(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)

    def test_Square_size_value_0(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    """-------- METHODS --------"""

    def test_Square_str(self):
        square = Square(1, 2, 3, 4)
        result = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(square), result)

    def test_Square_to_dictionary(self):
        square = Square(1, 2, 3, 4)
        result = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), result)

    def test_Square_update(self):
        square = Square(1, 2, 3, 4)
        square.update(5, 6, 7, 8)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 5)

    def test_Square_create(self):
        square = Square(1, 2, 3, 4)
        square_dictionary = square.to_dictionary()
        new_square = Square.create(**square_dictionary)
        self.assertEqual(str(square), str(new_square))

    def test_Square_save_to_file_exists_none(self):
        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')
        os.remove('Square.json')

    def test_Square_save_to_file_exists_empty(self):
        Square.save_to_file([])
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')
        os.remove('Square.json')

    def test_Square_save_to_file_exists(self):
        Square.save_to_file([Square(1)])
        with open('Square.json', 'r') as file:
            """
            ATTENTION:
                La valeur de votre id est differente de la mienne
                et elle est succeptible de changer a chaque execution.
                """
            self.assertEqual(
                file.read(), '[{"id": 23, "size": 1, "x": 0, "y": 0}]')
        os.remove('Square.json')

    def test_Square_load_from_file(self):
        square = Square(1, 2, 3, 4)
        Square.save_to_file([square])
        new_square = Square.load_from_file()
        self.assertEqual(str(square), str(new_square[0]))
