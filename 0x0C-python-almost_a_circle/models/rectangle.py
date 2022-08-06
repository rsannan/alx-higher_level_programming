#!/usr/bin/python3
"""This module defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This is the definition of Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the Rectangle object
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int): private instance attribute
                y (int): private instance attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates and returns the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle to stout"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")
