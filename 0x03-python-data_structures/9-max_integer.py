#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    big = my_list[0]
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]
    return big
