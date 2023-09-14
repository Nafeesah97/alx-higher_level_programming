#!/usr/bin/python3
"""
This module contains a function that reads a file
to stout
Author: Nafeesah
"""

def read_file(filename=""):
    """A function that reads file"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read())
