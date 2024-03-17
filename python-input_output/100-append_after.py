#!/usr/bin/python3

"""
    The ``13. Search and update`` module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        append_after - appends after specific string
    """
    new_text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    f.close()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_text)
    f.close()
