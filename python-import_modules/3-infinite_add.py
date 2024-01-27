#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sum_of_all = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            sum_of_all = sum_of_all + int(argv[i])
    print("{}".format(sum_of_all))
