#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argNum = len(argv) - 1
    sum = 0
    for i in range(1, argNum + 1):
        sum = sum + int(argv[i])
    print(sum)
