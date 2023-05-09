#!/usr/bin/python3
def print_last_digit(number):
    ''print last digit number''
    last_digit = abs(number) % 10
    print(f"{last_digit}", end='')
    return last_digit
