#!/usr/bin/python3
"""This defines a Square class"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
