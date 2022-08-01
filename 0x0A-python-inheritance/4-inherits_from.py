#!/usr/bin/python3
"""This module defines the inherits_from function"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class that
       inherited (directly or indirectly) from specified class
    """
    if isinstance(obj,  a_class) and type(obj) is not a_class:
        return True
    return False
