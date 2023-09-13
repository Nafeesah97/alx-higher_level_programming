#!/usr/bin/python3

"""
This module contains a lookup function.
It looks for a directory
Author: Nafeesah
"""


def lookup(obj):
    """Returns a list of available attributes and methods of obj"""
    res = []
    for items in dir(obj):
        res.append(items)
    return res
