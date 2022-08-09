#!/usr/bin/python3
"""This module defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize a new Square.
    Args:
        size(int) : The new width and height
        width (int): The width.
        height (int): The height.
        x (int): The x coordinate.
        y (int): The y coordinate.
        id (int): The identity of the Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        attrs_dict = {
            "id": self.id, "size": self.width,
            "x": self.x, "y": self.y
        }
        return attrs_dict

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Updates the values in Square instance
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
                    self.width = arg
                elif arg_count == 2:
                    self.x = arg
                elif arg_count == 3:
                    self.y = arg
                arg_count += 1
            return
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value
            return
