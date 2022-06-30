#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    index_num = 0
    if arg_num == 0:
        print("{:d} arguments.".format(arg_num))

    elif arg_num == 1:
        index_num += 1
        print("{:d} argument".format(arg_num))
        print("{:d}: {}".format(arg_num, sys.argv[index_num]))

    elif arg_num > 1:
        print("{:d} arguments".format(arg_num))
        for arg in range(arg_num):
            index_num += 1
            print("{:d}: {}".format(index_num, sys.argv[index_num]))
