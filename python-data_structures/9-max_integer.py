#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxil = my_list[0]
        for i in my_list:
            if i > maxil:
                maxil = i
        return maxil
    return None
