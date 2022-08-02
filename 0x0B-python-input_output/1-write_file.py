#!/usr/bin/python3
"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """ Writes to a file
        Args:
            filename (str): file to write to
            text (str): text to write
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
