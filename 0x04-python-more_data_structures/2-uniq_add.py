#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for number in set(my_list):
        sum = sum + number
    return sum
