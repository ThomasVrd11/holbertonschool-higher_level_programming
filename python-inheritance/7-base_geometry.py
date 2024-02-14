#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """class"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
