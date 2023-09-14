#!/usr/bin/python3

"""
This module contains a class
A class know as BaseGeometry
Author: Nafeesah
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle inherited from BaseGeometry

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle

    Methods:
        None

    """

    def __init__(self, width, height):
        """ Initializes private attributes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
