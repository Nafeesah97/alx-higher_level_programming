#!/usr/bin/python3

"""
This module contains a function
called is_same_class to check instances
Author: Nafeesah
"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
