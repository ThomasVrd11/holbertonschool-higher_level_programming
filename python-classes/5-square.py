#!/usr/bin/python3
"""define square class"""


class Square:
    """Square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size * self. __size

    @property
    def size(self):
        """Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for y in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print("")
