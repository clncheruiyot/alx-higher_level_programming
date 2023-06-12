#!/usr/bin/python3
"""The module inherits from the list class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
