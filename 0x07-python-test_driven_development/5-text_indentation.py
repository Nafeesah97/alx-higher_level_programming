#!/usr/bin/python3

"""
This module prints an argument
It contains a function that prints text passed toit
Author: Nafeesah
"""


def text_indentation(text):
    """
    Function that prints a text.
    
    Args:
        text(str): Text to be printed
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    modified = ""
    paragraph = ""

    text_mod = text.strip()
    for ch in text_mod:
        if ch == '.' or ch == '?' or ch == ':':
            paragraph += ch + "\n\n"
        else:
            paragraph += ch

    modified += paragraph
    print("{}".format(modified))
