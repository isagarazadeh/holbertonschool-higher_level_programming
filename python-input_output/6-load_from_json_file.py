#!/usr/bin/python3
'''
6-load_from_json_file.py
'''
import json


def load_from_json_file(filename):
    '''
    load_from_json_file creates an Object from a JSON file
    Args:
        filename: file name
    '''
    with open(filename, encoding="utf-8") as f:
        my_str = f.read()
    return json.loads(my_str)
