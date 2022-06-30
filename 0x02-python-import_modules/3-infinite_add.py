#!/usr/bin/python3
if __name__  == "__main__":
    import sys
    arg_num = len(sys.argv)
    total = 0
    for number in range(1, arg_num):
        total += int(sys.argv[number])

    print("{:d}".format(total))
