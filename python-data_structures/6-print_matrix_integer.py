#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j != i[len(i) - 1]:
                a = matrix(zip({[i], [j]))
    print("{}".format(a))
