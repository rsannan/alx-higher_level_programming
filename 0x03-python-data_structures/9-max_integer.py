#!/usr/bin/python3
def max_integer(my_list=[]):
    list_idx = len(my_list)
    max_num = 0
    if list_idx < 1:
        return

    for number in my_list:
        if number < max_num:
            continue
        max_num = number
    return max_num
