#!/usr/bin/python3

def no_c(my_string):
    updated_str = ''
    for a in my_string:
        if a != 'c' and a != 'C':
            updated_str += a
    return (updated_str)
