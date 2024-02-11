#!/usr/bin/python3
'''
3-to_json_string.py

'''
import json


def to_json_string(my_obj):
    '''
    to_json_string returns the JSON representation of an object
    Args:
        my_obj: object
    '''
    return json.dumps(my_obj)
