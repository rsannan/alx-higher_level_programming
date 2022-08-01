#!/usr/bin/python3
"""This module defines the MyList class"""


class MyList(list):
    """definition of a list subclass"""
    def print_sorted(self):
        """prints a sorted Mylist"""
        sort = self
        print(sorted(sort))
