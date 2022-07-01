#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        element1 = None

    else:
        element1 = sentence[0]
    return (str_len, element1)
