#!/usr/bin/python3
"""This module defines the read_file function"""


def read_file(filename=""):
    """ Reads a file
        Args:
            filename (str): file to read from
    """
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")
