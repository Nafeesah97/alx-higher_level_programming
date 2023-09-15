#!/usr/bin/python3
"""
importing json to deserialize
"""
import json

"""
This module contains a function
that converts  to python data from json
Author: Nafeesah
"""


def from_json_string(my_str):
    """To covert from json to python data"""
    data = json.loads(my_str)
    return data
