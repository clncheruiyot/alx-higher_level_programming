#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda p: p ** 2, row)) for row in matrix]
