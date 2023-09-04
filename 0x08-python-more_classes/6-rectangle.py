#!/usr/bin/python3

"""
This module contains a class Rectangle
Author: nafeesah
"""


class Rectangle:
    number_of_instances = 0
    """
    Represents a rectangle

    Attributes:
        width(int): Width of the rectangle
        height(int): The height of the rectangle

    Methods:
        area(): Finds the area of rectangle
        perimeter(): Finds the perimeter of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        perimeter = 0
        if self.width == 0 or self.height == 0:
            return perimeter
        else:
            perimeter = (self.width * 2) + (self.height * 2)
            return perimeter

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += ('#' * self.width) + '\n'
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

