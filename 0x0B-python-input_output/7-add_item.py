#!/usr/bin/python3
"""importing sys to get args"""
import sys

"""
importing json to deserialize
"""
import json

"""import modules needed"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
This module contains a file that can convert 
to/from json file
Author: Nafeesah
"""
filename = "add_item.json"
num_args = len(sys.argv)
ls = []
if num_args == 1:
    text = ls
if num_args > 1:
    i = 1
    while i < num_args:
        ls.append(sys.argv[i])
        text = ls
        i += 1

save_to_json_file(text, filename)
my_set = load_from_json_file(filename)
print(my_set)
