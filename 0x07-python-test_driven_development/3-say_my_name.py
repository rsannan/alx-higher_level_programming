#!/usr/bin/python3
"""This module defines the say_my_name function"""

def say_my_name(first_name, last_name=""):
    """Prints firstname and lastname

        Args:
            first_name (str): first name
            last_name (str): (optional) last name

        Returns:
            None 
            TypeError Otherwise
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    f_len = len(first_name)
    l_len = len(last_name)
    if f_len == 0 and l_len == 0:
        print("")

    elif l_len == 0:
        print("My name is {}".format(first_name))

    else:
        print("My name is {} {}".format(first_name, last_name))
