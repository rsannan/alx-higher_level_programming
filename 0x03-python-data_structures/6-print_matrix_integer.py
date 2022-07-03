#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for mat_list in matrix:
            if isinstance(mat_list, list):
                if len(mat_list) == 0:
                    continue
                for number in mat_list:
                    if mat_list[-1] == number:
                        print("{:d}".format(number),)
                    else:
                        print("{:d}".format(number), end=" ")
