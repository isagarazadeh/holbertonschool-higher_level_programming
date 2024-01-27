#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    secrets = dir(hidden_4)
    for i in secrets:
        if i[0] != "_" or i[1] != "_":
            print("{}".format(i))
