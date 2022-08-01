#!/usr/bin/python3
"""This module defines the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """Intialize a new Rectangle.
        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
