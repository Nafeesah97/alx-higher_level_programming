#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    res = dir(hidden_4)
    for item in res:
        if "__" in item:
            pass
        else:
            print("{}".format(item))
