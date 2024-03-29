#!/usr/bin/python3
"""This modules defines is_same_class"""


def is_same_class(obj, a_class):
    """returns true if object is exactly the same instance
       of the specified class
    """
    return type(obj) is a_class
