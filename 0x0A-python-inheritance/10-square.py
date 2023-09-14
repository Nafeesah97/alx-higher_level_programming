#!/usr/bin/python3

"""
This module contains a class
A class know as BaseGeometry
Author: Nafeesah
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle.

    Attributes:
        size(int): length of rectangle

    Methods:
        area(): area of square
    """

    def __init__(self, size):
        """to initialize size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area"""
        return (self.__size * self.__size)
