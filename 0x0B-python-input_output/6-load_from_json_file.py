#!/usr/bin/python3
"""
importing json to deserialize
"""
import json

"""
This module contains a function that converts json to data
and writes it into a file
Author: Nafeesah
"""


def load_from_json_file(filename):
    """converts json file to data"""
    with open(filename, "r") as file:
        data = json.load(file)
        return data
