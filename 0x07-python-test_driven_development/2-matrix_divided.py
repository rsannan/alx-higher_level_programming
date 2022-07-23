#!/usr/bin/python3
"""This module defines the matrix_divide function"""

def matrix_divided(matrix, div):
    """Divides all the elements of a matrix

        Args:
            matrix (list): 2D nested list of int/floats
            div (int/float): number to divide by

        Returns:
            a nested list of divided elements
            TypeError, ZeroDivisionError Otherwise
    """
def matrix_divided(matrix, div):
    bool_mat = not isinstance(matrix, list)
    bool_matlist = not all(isinstance(element, list) for element in matrix)
    if (bool_mat or bool_matlist):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    matele = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
    bool_matele = not all(isinstance(num, (int, float)) for num in matele)

    if (bool_matele):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    
    for i in range(len(matrix)):
        list_matrix = []
        if i == 0:
            match_matrix = len(matrix[i])
        else: 
            match_matrix = len(matrix[i- 1])
            
        if match_matrix != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            if not isinstance(div, (int, float)):
                raise TypeError('div must be a number')
            elif div == 0:
                raise ZeroDivisionError('division by zero')
            else:
                number = matrix[i][j] / div
                list_matrix.append(round(number, 2))
        new_matrix.append(list_matrix)  
    return new_matrix
