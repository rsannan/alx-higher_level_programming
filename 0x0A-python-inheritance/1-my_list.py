#!/usr/bin/python3
"""This modules defines MyList class"""


class MyList(list):
    """MyList class subclass of list"""
    def print_sorted(self):
        """prints a sorted MyList"""
        a = self
        print(sorted(a))
