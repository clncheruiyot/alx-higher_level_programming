#!/usr/bin/python3
"""This script defines an algorithm for finding peaks in a list of integers."""

def find_peak(list_of_integers):
    """Finds the peak within a list of integers."""
    if not list_of_integers:
        return None
    
    length = len(list_of_integers)
    middle = int(length / 2)
    integer_list = list_of_integers

    if middle - 1 < 0 and middle + 1 >= length:
        return integer_list[middle]
    elif middle - 1 < 0:
        return integer_list[middle] if integer_list[middle] > integer_list[middle + 1] else integer_list[middle + 1]
    elif middle + 1 >= length:
        return integer_list[middle] if integer_list[middle] > integer_list[middle - 1] else integer_list[middle - 1]

    if integer_list[middle - 1] < integer_list[middle] > integer_list[middle + 1]:
        return integer_list[middle]

    if integer_list[middle + 1] > integer_list[middle - 1]:
        return find_peak(integer_list[middle:])
    return find_peak(integer_list[:middle])
