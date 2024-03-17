#!/usr/bin/python3
'''
Documentation
'''

if __name__ == "__main__":
    import sys
    s_c = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
           "404": 0, "405": 0, "500": 0}
    file_size = 0
    count = 0
    same = False
    while True:
        try:
            string = input()
            x = string.split()
            for j in x:
                if j.isdigit() and j in s_c.keys() and same is False:
                    s_c[j] += 1
                    same = True
                elif j.isdigit():
                    file_size += int(j)
            same = False
            count += 1
            if count == 10:
                print("File size: {}".format(file_size))
                for i in s_c.keys():
                    if s_c[i] > 0:
                        print("{}: {}".format(i, s_c[i]))
                count = 0
        except (KeyboardInterrupt, EOFError):
            print("File size: {}".format(file_size))
            for i in s_c.keys():
                if s_c[i] > 0:
                    print("{}: {}".format(i, s_c[i]))
            break
