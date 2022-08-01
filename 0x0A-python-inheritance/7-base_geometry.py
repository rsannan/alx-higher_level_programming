#!/usr/bin/python3
"""This module contains BaseGeometry class"""


class BaseGeometry():
    """This is a geometry class"""
    def __init__(self):
        """initializing the class"""
        pass

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer
            Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
