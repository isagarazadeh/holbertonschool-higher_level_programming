#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    for i in set_1:
        for j in set_2:
            if j != i:
                od_set.append(i)
    return od_set
