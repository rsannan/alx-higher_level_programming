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

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates the values in Rectangle instance
            Args:
                args (list): to allow variable number of arguments
                kwargs (dict): to allow variable number of keyword args
        """
        if len(args) > 0:
            arg_count = 0
            for arg in args:
                if arg_count == 0:
                    self.id = arg
                elif arg_count == 1:
                    self.__width = arg
                elif arg_count == 2:
                    self.__height = arg
                elif arg_count == 3:
                    self.__x = arg
                elif arg_count == 4:
                    self.__y = arg
                arg_count += 1
            return
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                elif key == "width":
                    self.__width = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
                elif key == "id":
                    self.id = value
            return
