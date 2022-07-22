#!/usr/bin/python3
"""This module defines the add function."""


def add_integer(a, b=98):
    """Adds two numbers

        Args:
            a (int): first number(coverted to int if float)
            b (int): second number(converted to int if float)

        Returns:
            integer addition of a & b on Success
            TypeError Otherwise
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
