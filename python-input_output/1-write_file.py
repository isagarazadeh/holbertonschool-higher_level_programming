#!/usr/bin/python3
'''
1-write_file.py

'''


def write_file(filename="", text=""):
    '''
    write_file writes text into a file
    Args:
        filename: file name
        text: text
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
