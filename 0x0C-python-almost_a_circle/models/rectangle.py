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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def width(self, value):
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.y = value
