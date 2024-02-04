#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listofitems = sorted(a_dictionary.items())
    for i in listofitems:
        print("{}: {}".format(i[0], i[1]))
