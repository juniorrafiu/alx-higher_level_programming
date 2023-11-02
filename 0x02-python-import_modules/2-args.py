#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argNum = len(argv) - 1
    if argNum == 1:
        print('{} argument:'.format(argNum))
    else:
        print('{} arguments:'.format(argNum))
    for i in range(1, argNum + 1):
        print('{}: {}'.format(i, argv[i]))
