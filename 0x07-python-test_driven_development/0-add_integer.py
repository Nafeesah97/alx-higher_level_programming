#!/usr/bin/python3

"""
This module for performing mathematical operations
This module provides functions for addition
Author: Nafeesah
"""
def add_integer(a, b=98):
    """
    Adds 2 integers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    result = int(a) + int(b)
    return result
