#!/usr/bin/python3
"""BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """return string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
