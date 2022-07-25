#!/usr/bin/python3
"""This defines a Rectangle class"""


class Rectangle:
    """This is a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        read_str = []
        for i in range(self.__height):
            for j in range(self.__width):
                read_str.append(str(self.print_symbol))
            if i != (self.__height - 1):
                read_str.append("\n")
        return("".join(read_str))

    def __repr__(self):
        return('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        rect1_area = rect_1.area()
        rect2_area = rect_2.area()
        if (rect1_area >= rect2_area):
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
