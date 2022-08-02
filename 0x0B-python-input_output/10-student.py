#!/usr/bin/python3
"""This module defines the Student class"""


class Student():
    """Student class definition"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
            a Student instance

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
           all(type(items) == str for items in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
