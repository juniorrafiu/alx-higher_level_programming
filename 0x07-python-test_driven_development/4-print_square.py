#!/usr/bin/python3
def print_square(size):
    """this function prints a square of length size
        the size value must be an integer
        size should be >= 0"""
    if not isinstance(size,int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for column in range(size):
        for row in range(size):
            print("#", end ="")
        print("")
