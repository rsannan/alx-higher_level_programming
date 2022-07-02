#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for mat_list in matrix:
            for number in mat_list:
                if mat_list[-1] == number:
                    print("{:d}".format(number),)
                else:
                    print("{:d}".format(number), end=" ")
