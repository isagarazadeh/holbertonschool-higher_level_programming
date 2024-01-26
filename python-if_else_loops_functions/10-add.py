#!/usr/bin/python3
def add(a, b):
    if b < 0:
        b = -1 * (-1 * b)
    elif a < 0:
        a = -1 * (-1 * a)
    c = a + b
    print("{}".format(c), end="")
    return c
