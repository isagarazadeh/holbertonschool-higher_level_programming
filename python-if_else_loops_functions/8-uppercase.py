#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            result = result + chr(ord(char) - 32)
        else:
            result = result + i
    print("{}".format(result))
