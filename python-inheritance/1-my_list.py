#!/usr/bin/python3
'''
MyModule
'''


class MyList(list):
    '''
    List inherited
    '''
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
