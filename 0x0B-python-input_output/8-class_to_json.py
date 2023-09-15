#!/usr/bin/python3
"""
importing json to serialize
"""
#import json

"""
This module contains a function
that converts  to class from json
Author: Nafeesah
"""


def class_to_json(obj):
    """function to convert instance attributes to json """
    data = obj.__dict__
    #json_data = json.dumps(data)
    return data