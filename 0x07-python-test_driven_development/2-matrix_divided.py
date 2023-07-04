#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ this function takes in a matrix and divides each member of the matrix by div
    args: matrix: a list of list of integers or floats
          div : divisor
          raises TypeError when members of matrix are not int or float
          raises TypeError when rows of matrix are of different sizes
          raises TypeError when div is not a float or int
          raises ZeroDivisionError when div is 0
          Returns a new matrix with results"""
    if (not isinstance(div,(float,int))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix,list) or matrix == [] or
        not all(isinstance(row,list) for row in matrix) or
        not all(isinstance(member,(float,int))for member in [element for row in matrix for element in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not all(len(matrix[0])==len(row)for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x : round(x/div,2),row)) for row in matrix])
