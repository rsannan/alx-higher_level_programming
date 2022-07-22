#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list)
        or not all(isinstance(element, list) for element in matrix)):
        #or not isinstance(matrix[i][j], (int, float))
        #for i in matrix for j in range(len(matrix[i]))):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    for i in range(len(matrix)):
        list_matrix = []
        for j in range(len(matrix[i])):
            if isinstance(div, (int, float)) or\
                div != 0:
                number = matrix[i][j] / div
                list_matrix.append(round(number, 2))
        new_matrix.append(list_matrix)
    return new_matrix
