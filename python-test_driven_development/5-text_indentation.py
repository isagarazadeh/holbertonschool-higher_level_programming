#!/usr/bin/python3
'''
This module includes a function that replace '.', ':', '?' with 2 new lines
'''


def text_indentation(text):
    '''
    text_indentation replaces '.', ':', '?' with 2 new lines

    Args:
        text: text
    '''
    flag = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if flag and text[i].isspace():
            continue
        elif text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
            flag = True
        else:
            print(text[i], end="")
            flag = False
