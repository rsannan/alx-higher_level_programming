#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    list_idx = len(my_list) - 1
    if idx < 0 or idx > list_idx:
        return my_list

    new_list[idx] = element
    return new_list
