#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tupa = tuple_a + (0, 0)
    new_tupb = tuple_b + (0, 0)
    element1 = new_tupa[0] + new_tupb[0]
    element2 = new_tupa[1] + new_tupb[1]
    new_tup = (element1, element2)
    return new_tup
