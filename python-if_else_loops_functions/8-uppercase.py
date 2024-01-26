#!/usr/bin/python3
def uppercase(str):
    if ord(str) > 96 and ord(str) < 123:
        str = str - 32
        print("{}".format(str))
