#!/usr/bin/python3

"""
This module is used to print square
The function prints the character ~ to compute square
Author: Nafeesah
"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size(int): size of the square side
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
