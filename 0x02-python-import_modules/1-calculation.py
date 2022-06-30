#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    add_total = calc.add(a, b)
    sub_total = calc.sub(a, b)
    mul_total = calc.mul(a, b)
    div_total = calc.div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_total))
    print("{:d} - {:d} = {:d}".format(a, b, sub_total))
    print("{:d} * {:d} = {:d}".format(a, b, mul_total))
    print("{:d} / {:d} = {:d}".format(a, b, div_total))
