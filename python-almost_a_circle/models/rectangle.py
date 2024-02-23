#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class to define Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Description:
            A function to initialize a Rectangle object.

        Attributes:
            width (int) : The width of the rectangle.
            height (int) : The height of the rectangle.
            x (int)
            y (int)
            id (int) : The id of the object.

        Calls:
            super().__init__(id) : Calls the constructor of Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Description:
            (G) A function to get the width of the rectangle.

        Returns:
            The width of the rectangle. (int)
        """
        return self.__width

    @property
    def height(self):
        """
        Description:
            (G) A function to get the height of the rectangle.

        Returns:
            The height of the rectangle. (int)
        """
        return self.__height

    @property
    def x(self):
        """
        Description:
            (G) A function to get the x of the rectangle.

        Returns:
            The x (int)
        """
        return self.__x

    @property
    def y(self):
        """
        Description:
            (G) A function to get the y  of the rectangle.

        Returns:
            The y (int)
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Description:
            A function to set the width of the rectangle.

        Args:
            value (int) : The value to set the width to.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Description:
            A function to set the height of the rectangle.

        Args:
            value (int) : The value to set the height to.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Description:
            A function to set the x of the rectangle.

        Args:
            value (int) : The value to set the x to.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        Description:
            A function to set the y of the rectangle.

        Args:
            value (int) : The value to set the y to.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Description:
            Calculates the area (width * height) of the rectangle.

        Returns:
            The area of the rectangle. (int)
        """
        return self.__width * self.__height

    def display(self):
        """Description:
            Prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """
        Description:
            Returns a formal string representation of the rectangle.
            EX :  Rectangle(2, 4)

        Returns:
            The formal string representation of the rectangle. (str)
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Description:
            Updates the values of the rectangle with the given arguments.
            If args is not empty, the first argument is the id,
            the second is the width, the third is the height,
            the fourth is the x, and the fifth is the y.

            If args is empty or doesn't, the arguments are passed as kwargs.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                if i == "width":
                    self.__width = kwargs[i]
                if i == "height":
                    self.__height = kwargs[i]
                if i == "x":
                    self.__x = kwargs[i]
                if i == "y":
                    self.__y = kwargs[i]

    def to_dictionary(self):
        """
        Description:
            Returns the dictionary representation of a Rectangle.

        Returns:
            The dictionary representation of a Rectangle. (dict)
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
