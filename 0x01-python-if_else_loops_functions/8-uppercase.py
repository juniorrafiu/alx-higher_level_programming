#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            char = chr(ord(i) - 32)
        else:
            char = i
        print(f'{char}', end = "")
    print('')
