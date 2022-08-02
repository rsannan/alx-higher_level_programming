#!/usr/bin/python3
"""This module defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”
        Args:
            filename (str): file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return json.load(myfile)
