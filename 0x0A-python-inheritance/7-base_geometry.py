#!/usr/bin/python3

"""
This module contains a class
A class know as BaseGeometry
Author: Nafeesah
"""


class BaseGeometry():
    """
    A class named BaseGeometry.

    Attribute:
        name(str): name of geom
        value(int): value of name

    Method:
        area(): computes area of geometry
        integer_validator(): validate if value is an integer or not
    """

    def area(self):
        """To check area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
