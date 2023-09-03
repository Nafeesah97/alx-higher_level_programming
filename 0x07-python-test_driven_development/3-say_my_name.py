#!/usr/bin/python3

"""
This module is used to print
It contains a function that prints firstname and last name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is first_name Last_name

    Args:
        first_name(str): first_name
        last_name(str): last_name(an optional argument)

    Returns:
        str: My name is first_name Last_name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

