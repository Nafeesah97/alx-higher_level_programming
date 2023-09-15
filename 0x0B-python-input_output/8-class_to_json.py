#!/usr/bin/python3
"""
This module contains a function
that converts  to class from json
Author: Nafeesah
"""


def class_to_json(obj):
    """function to convert instance attributes to json """
    data = obj.__dict__
    return data
