#!/usr/bin/python3
def add_integer(a, b=98):
    """ this function is going to add two integers
    if a and b are floats then cast it into an integer
    if a and b is not integer or float then raise TypeError"""

    if (not isinstance(a,(int,float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b,(int,float))):
        raise TypeError("b must be an integer")
    if isinstance(a,float):
        a=int(a)
    if isinstance(b,float):
        b=int(b)
    return (a+b)
