#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.keys())
    for key in new_dict:
        print("{} : {}".format(key, a_dictionary[key]))
    
