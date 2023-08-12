#!/usr/bin/python3
import sys, hidden_4
res = dir(hidden_4)
for item in res:
    if "__" in item:
        pass
    else:
        print("{}".format(item))
