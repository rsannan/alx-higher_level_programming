#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat_list in matrix:
        if len(mat_list) == 0:
            continue
        for number in mat_list:
            if mat_list[-1] != number:
                print("{:d}".format(number), end=" ")
            else:
                print("{:d}".format(number), end=" ")
                print("")
