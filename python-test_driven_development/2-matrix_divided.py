#!/usr/bin/python3
'''
This module has a function that divides elements of matrix
'''


def matrix_divided(matrix, div):
    '''
    matrix_divided divides matrix elements

    Args:
        matrix: matrix of integers or floats
        div: divider
    '''
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    error_msg2 = "Each row of the matrix must have the same size"
    error_msg3 = "div must be a number"
    error_msg4 = "division by zero"
    new_list = []
    count = 0
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(error_msg3)
    if div == 0:
        raise ZeroDivisionError(error_msg4)
    for j in matrix:
        len1 = len(matrix[0])
        if len1 != len(j):
            raise TypeError(error_msg2)
        new_list.append([])
        for i in j:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError(error_msg)
            new_list[count].append(round(i / div, 2))
        count += 1
    return new_list
