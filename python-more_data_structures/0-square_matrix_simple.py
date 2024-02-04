#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    k = 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[k].append(j ** 2)
        k = k + 1
    return new_matrix
