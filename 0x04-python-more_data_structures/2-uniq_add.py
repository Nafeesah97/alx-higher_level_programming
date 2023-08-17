#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    res = 0
    for item in new_set:
        res += item
    return res
