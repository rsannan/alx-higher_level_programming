#!/usr/bin/python3
"""This module defines the is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance or if the object is an instance of
       a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
