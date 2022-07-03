#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for l in range(len(matrix[i])):
            if matrix[i][-1] != matrix[i][l]:
                print("{:d}".format(matrix[i][l]), end="")
                print(" ", end="")
            else:
                print("{:d}".format(matrix[i][l]))
