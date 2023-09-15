#!/usr/bin/python3
"""
importing json to serialize
"""
import json

"""
This module contains a function that converts data to json
and writes it into a file
Author: Nafeesah
"""


def save_to_json_file(my_obj, filename):
    """A function to convert to json and write into a file"""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
