#!/usr/bin/python3
"""This module defines print_square function"""


def print_square(size):
    """Prints a square with the character '#'

        Args:
            size (int): size of the square

        Returns:
            None
            TypeError, ValueError Otherwise
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
