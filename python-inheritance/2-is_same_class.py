#!/usr/bin/python3
'''
MyModule_3
'''


def is_same_class(obj, a_class):
    '''
    is_same_class checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class
    '''
    return type(obj) is a_class
