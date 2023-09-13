#!/usr/bin/python3

"""
This module contains a function that checks if an object is an instance of a
class or a subclass
Author: Nafeesah
"""


def inherits_from(obj, a_class):
    """check instance of a class"""
    for subclass in obj.__class__.mro():
        if subclass is not a_class and issubclass(subclass, a_class):
            return True
        else:
            return False
