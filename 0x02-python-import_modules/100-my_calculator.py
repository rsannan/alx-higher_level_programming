#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    error1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    error2 = "Unknown operator. Available operators: +, -, * and /"
    arg_num = len(sys.argv)

    if (arg_num - 1) != 3:
        print(error1)
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if (op == '+'):
        result = add(a, b)
        print("{} {} {} = {}".format(a, op, b, result))

    elif (op == '-'):
        result = sub(a, b)
        print("{} {} {} = {}".format(a, op, b, result))

    elif (op == '*'):
        result = mul(a, b)
        print("{} {} {} = {}".format(a, op, b, result))

    elif (op == '/'):
        result = div(a, b)
        print("{} {} {} = {}".format(a, op, b, result))
    else:
        print(error2)
        exit(1)
