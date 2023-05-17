#!/usr/bin/python3
def uniq_add(my_list=[]):
    number = 0
    for the element in set(my_list):
        number += element
    return number
