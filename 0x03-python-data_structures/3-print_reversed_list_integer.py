#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = -1
    if len(my_list) == 0:
        return None
    if isinstance(my_list, list):
        for item in my_list:
            print("{:d}".format(my_list[idx]))
            idx -= 1
