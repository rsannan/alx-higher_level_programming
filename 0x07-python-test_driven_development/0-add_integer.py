#!/usr/bin/python3
"""
Module contains add function
This module defines the add function.
This functions adds two ints or floats and returns int
"""


def add_integer(a, b=98):
    """
        Adds two numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
