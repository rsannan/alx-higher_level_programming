#!/usr/bin/python3
"""This defines a Square class"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
           size(int): Size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and not all(value) >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__size = value

    def area(self):
        """Returns the Area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self.__position[1] < 0:
                    for k in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
