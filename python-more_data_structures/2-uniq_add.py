#!/usr/bin/python3
def uniq_add(my_list=[]):
    reduced = set(my_list)
    summa = 0
    for i in reduced:
        summa += i
    return summa
