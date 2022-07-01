#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = -1
    for index in range(len(my_list)):
        print("{:d}".format(my_list[idx]))
        idx -= 1
