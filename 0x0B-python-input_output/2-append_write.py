#!/usr/bin/python3

""""
This module contains a funcrion
that wirtes/appends something into a file
Author: Nafeesah
"""


def append_write(filename="", text=""):
    """writes/appends a text into a file"""
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
