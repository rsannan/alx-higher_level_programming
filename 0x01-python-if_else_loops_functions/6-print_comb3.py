#!/usr/bin/python3
for number1 in range(0,  10):
    for number2 in range(0, 10):
        if (number1 * 10) + number2 == 89:
            print("{}".format((number1 * 10) + number2))
        elif number1 < number2:
            print("{:02d}".format((number1 * 10) + number2), end=", ")
