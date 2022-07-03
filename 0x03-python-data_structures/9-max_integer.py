#!/usr/bin/python3
def max_integer(my_list=[]):
    list_idx = len(my_list)
    max_num = my_list[0]
    if list_idx == 0:
        return None

    if isinstance(my_list, list):
        for number in my_list:
            if number < max_num:
                continue
            max_num = number
        return max_num
