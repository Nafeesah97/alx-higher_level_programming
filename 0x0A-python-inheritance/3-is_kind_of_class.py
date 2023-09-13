#!/usr/bin/python3

"""
This module contains a function that checks if the object is an instance of
or if the object is an instance of a class that inherited from, the specified
class
"""


def is_kind_of_class(obj, a_class):
    """checks the kind of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
