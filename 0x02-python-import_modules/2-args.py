#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argNum = len(argv) - 1
    if argNum == 1:
        print('{} argument:\n'.format(argNum))
    else:
        print('{} arguments:\n'.format(argNum))
    for i in range(argNum):
        print('{}: {}:\n'.format(i, argv[i]))
