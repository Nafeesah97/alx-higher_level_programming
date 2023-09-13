#!/usr/bin/python3

"""
This module contains myList that inherits from list.
The list is assume to contain only integers
Author: Nafeeesah
"""


class MyList(list):
    """
    This class inherits from list.

    Attributes:
        ls(int): list inherited

    Methods:
        print_sorted(): prints the list, but sorted (ascending sort)

    Examples:
        mylist = [4, 3, 5]
        print_sorted(my_list)

        [3, 4, 5]
    """

    def print_sorted(self):
        res = sorted(self)
        print("{}".format(res))
