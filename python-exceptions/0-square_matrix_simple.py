#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    x = 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[x].append(j**2)
        x += 1
    return new_matrix
