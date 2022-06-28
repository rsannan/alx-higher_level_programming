#!/usr/bin/python3
def make_upper(letter):
    if 96 < ord(letter) < 123:
        return(chr(ord(letter) - 32))
    else:
        return(chr(ord(letter)))


def uppercase(str):
    upper_string = ""
    for letter in str:
        upper_string += "%c" % make_upper(letter)
    print("{}".format(upper_string))
