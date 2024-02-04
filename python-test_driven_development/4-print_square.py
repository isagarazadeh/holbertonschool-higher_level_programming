#!/usr/bin/python3
'''
This module has a function that prints a square.
'''


def print_square(size):
    '''
    print_square prints a square.

    Args:
        size: size of the square.
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
