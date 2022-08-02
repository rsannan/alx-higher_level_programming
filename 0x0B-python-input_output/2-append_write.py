#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """ appends to a file
        Args:
            filename (str): file to write to
            text (str): text to write
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
