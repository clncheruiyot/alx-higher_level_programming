#!/usr/bin/python3
"""Module defines the text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as t:
        for line in t:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "q") as q:
        w.write(text)
