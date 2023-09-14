#!/usr/bin/python3

""""
This module contains a funcrion
that wirte/overwrites something into a file
Author: Nafeesah
"""

def write_file(filename="", text=""):
    """writes a text into a file"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(text)
        