#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) - 1 == 0:
        print("{} arguments.".format(len(argv)))
    elif len(argv) - 1 == 1:
        print("{} argument:".format(len(argv)))
    else:
        print("{} arguments:".format(len(argv)))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
