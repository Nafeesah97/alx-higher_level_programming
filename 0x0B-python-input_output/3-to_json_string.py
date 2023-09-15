#!/usr/bin/python3
"""
importing json to serialize
"""
import json

"""
This module contains a function
that converts data to json
Author: Nafeesah
"""


def to_json_string(my_obj):
    """To returns the JSON representation of an object (string)"""
    data = json.dumps(my_obj)
    return data
