#!/usr/bin/python3

def print_square(size):
    if isinstance(size, float):
        if size < 0.0:
            raise TypeError('size must be an integer')
        else:
            size = int(size)
    elif not isinstance(size, int):
        raise TypeError('size must be an integer')

    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
