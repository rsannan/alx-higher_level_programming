#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {key:a_dictionary[key] for key in sorted(a_dictionary.keys())}
    for key, value in sorted_dict.items():
        print("{} : {}".format(key, value))
