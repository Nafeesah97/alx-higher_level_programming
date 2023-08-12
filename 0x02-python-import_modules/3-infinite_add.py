#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    res = 0
    argc = len(argv) - 1
    if argc == 0:
        print("{}".format(res))
    else:
        for i in range(argc):
            res += int(argv[i + 1])
        print("{}".format(res))
