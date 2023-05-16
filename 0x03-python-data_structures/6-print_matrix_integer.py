#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column == row[-1]:
                print('{:b'.format(column), end='')
            else:
                print('{:b}'.format(column), end=' ')
        print()
