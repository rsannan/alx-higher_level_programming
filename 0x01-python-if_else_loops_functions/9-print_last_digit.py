#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new_number = number * -1
    else:
        new_number = number

    last_digit = new_number % 10
    print("{:d}".format(last_digit), end="")
    return(last_digit)
