#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tflist = []
    for i in my_list:
        if i % 2 == 0:
            tflist.append(True)
        else:
            tflist.append(False)
    return tflist
