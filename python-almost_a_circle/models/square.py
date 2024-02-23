#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class to define Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Description:
            A function to initialize a Square object.

        Attributes:
            size (int) : The size of the square (width and height).
            x (int)
            y (int)
            id (int) : The id of the object.

        Calls:
            super().__init__(id) : Calls the constructor of Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Description:
            A function to return the string representation of the object.

        Returns:
            The string representation of the object. (str)
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Description:
            (G) A function to get the size of the square.

        Returns:
            The size of the square. (int)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Description:
            A function to set the size of the square.

        Attributes:
            value (int) : The size of the square.

        Calls:
            self.width = value : Calls the setter of width.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Description:
            A function to update the attributes of the object.

        Attributes:
            *args (list) : A list of arguments.
            **kwargs (dict) : A dictionary of arguments.

        Calls:
            super().update(*args, **kwargs) : Calls the update
            of Rectangle class.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                if i == "size":
                    self.size = kwargs[i]
                if i == "x":
                    self.x = kwargs[i]
                if i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        """
        Description:
            Returns the dictionary representation of a Rectangle.

        Returns:
            The dictionary representation of a Rectangle. (dict)
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
