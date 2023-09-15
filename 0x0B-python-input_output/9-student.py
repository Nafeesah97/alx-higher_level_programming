#!/usr/bin/python3
"""
This module contains a class that contains a function
that converts  to class from json
Author: Nafeesah
"""


class Student(self):
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

    def to_json(self):
        """a function for class to json"""
        return (self.__dict__)
    