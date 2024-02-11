#!/usr/bin/python3
'''
12-pascal_triangle.py


'''


def pascal_triangle(n):
    '''
    pascal_triangle returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n: integer
    '''
    my_list = []
    for i in range(n):
        if i == 0:
            my_list.append([1])
        elif i == 1:
            my_list.append([1, 1])
        else:
            prev_list = my_list[i - 1]
            new_list = [1]
            for x in range(len(prev_list) - 1):
                new_list.append(prev_list[x] + prev_list[x + 1])
            new_list.append(1)
            my_list.append(new_list)
    return my_list
