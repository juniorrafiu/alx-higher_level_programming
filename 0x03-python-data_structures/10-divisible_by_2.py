#!/usr/bin/python3
# 10-divisible_by_2.py
def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        if i % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
