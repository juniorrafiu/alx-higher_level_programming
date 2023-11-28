#!/usr/bin/python3
"""
Module contains a function that adds 2 integers
"""


def add_integer(a, b=98):
    """ a function that adds two integers
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
