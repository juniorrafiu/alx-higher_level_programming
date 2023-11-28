#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ it divides elements of matrix by div"""
    new_matrix = []
    if isinstance(div, int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")

    for row in matrix:
        if isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
        else:
            no_of_rows = len(matrix)
            length = no_of_rows - 1

        for i in range(length):
            if len(matrix[x]) != len(matrix[x + 1]):
                raise TypeError("Each row of the matrix\
                        must have the same size")

        inner_matrix = []
        for i in row:
            if isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix\
                        (list of lists) of integers/floats')
            val = round(matrix[row][i] / div, 2)
            inner_matrix.append(val)

        new_matrix.append(inner_matrix)
        return new_matrix
