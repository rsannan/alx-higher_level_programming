#!/usr/bin/python3
"""This module defines the lookup function"""


def lookup(obj):
    """This function returns a list of available
    attributes and methods of an object
    args:
        @obj: object to search

    Return: A list
    """
    return [method_name for method_name in dir(obj)]
