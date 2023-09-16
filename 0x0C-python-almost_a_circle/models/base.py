#!/usr/bin/python3

"""
This module contains the class base that
is used to instantiate the id
Author: Nafeesah
"""


class Base:
    """
    This is class named Base.

    Attributes:
        nb_objects(int): number of instances
        id(int): id of class instances

    Methods:
        None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """To instantiate object attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
