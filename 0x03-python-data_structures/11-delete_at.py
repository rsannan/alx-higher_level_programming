#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    list_idx = len(my_list)
    if idx < 0 or (list_idx - 1) < idx:
        return my_list

    for item in range(list_idx):
        if item == idx:
            continue
        new_list.append(my_list[item])

    my_list.clear()
    for item in new_list:
        my_list.append(item)
    return my_list
