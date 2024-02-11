#!/usr/bin/python3
'''
7-add_item.py


'''
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args = sys.argv

try:
    my_prev = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_prev = []

for i in range(1, len(args)):
    my_prev.append(args[i])

save_to_json_file(my_prev, "add_item.json")
