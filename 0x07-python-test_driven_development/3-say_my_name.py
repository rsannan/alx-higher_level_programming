#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    f_len = len(first_name)
    l_len = len(last_name)
    if f_len == 0 and l_len == 0:
        print("")

    elif l_len == 0:
        print("My name is {}".format(first_name))

    else:
        print("My name is {} {}".format(first_name, last_name))
