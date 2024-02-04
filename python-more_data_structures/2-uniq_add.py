#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = []
    summa = 0
    result = my_list.reduce()
    for i in result:
        summa += i
    print("Result: ".format(summa))
