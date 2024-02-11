#!/usr/bin/python3
'''
Has a function that returns the dictionary description with
simple data structure for JSON serialization of an object
'''


def class_to_json(obj):
    '''
    class_to_json returns the dictionary description with
    simple data structure for JSON serialization of an object

    Args:
        obj: object
    '''
    return obj.__dict__
