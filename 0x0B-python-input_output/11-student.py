#!/usr/bin/python3
"""
This module contains a class that contains a function
that converts  to class from json
Author: Nafeesah
"""


class Student:
    """
    a class called student

    Attributes:
        first_name(str): The first name of student
        last_name(str): The family name of student
        age(int): The age of student

        Methods:
            to_json(): retrieves a dictionary representation of a Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a function for class to json"""
        json_dat = {}
        if type(attrs) is list:
            for item in attrs:
                if item in self.__dict__:
                    json_dat[item] = self.__dict__[item]
            return json_dat
        return (self.__dict__)
    
    def reload_from_json(self, json):
        """a function to convert from json to data"""
        for key, value in json.items():
            self.__dict__[key] = json[key]
