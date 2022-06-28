#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 96 < ord(letter) < 123:
            print("{}".format(chr(ord(letter) - 32 )), end="")
        else:
            print("{}".format(letter), end="")
