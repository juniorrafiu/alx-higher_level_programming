#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -2):
    print(f'{chr(i)}{chr(i-33)}', end = "")
