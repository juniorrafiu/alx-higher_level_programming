#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import random
    if (len(sys.argv)-1 == 0):
        print("0 arguments.")
    else:
        if (len(sys.argv)-1 == 1):
            print("1 argument:")
            print("{}: {}".format(1, sys.argv[1]))
        elif (len(sys.argv)-1 > 1):
            print("{} arguments:".format(len(sys.argv)-1))
            for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))
