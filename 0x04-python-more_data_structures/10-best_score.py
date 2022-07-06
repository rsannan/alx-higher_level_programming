#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return

    large_num = 0
    for key, value in a_dictionary.items():
        if value > large_num:
            dict_tup = (key, value)
            large_num = value

    return dict_tup[0]
