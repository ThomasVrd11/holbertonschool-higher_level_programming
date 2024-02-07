#!/usr/bin/python3
""" define rectangle """


class Rectangle:
    """ define rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        if self.width == 0 or self.height == 0:
            self.area = 0
        return (self.width * self.height)

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            self.perimeter = 0
            return self.perimeter
        return ((self.width * 2) + (self.height * 2))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                print(self.print_symbol, end="")
            if i != self.height - 1:
                print()
        return ''

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
