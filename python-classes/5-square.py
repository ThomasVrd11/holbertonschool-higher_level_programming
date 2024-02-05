#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
