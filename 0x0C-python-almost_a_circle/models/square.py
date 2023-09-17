#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This module contains a class named rectangle
Author: Nafeesah
"""


class Square(Rectangle):
    """
    A class named square inherited from Rectangle

    Attributes:
        size(int): length of one side of square
        x(int): the horizontal axis
        y(int): the vertical axis
        id(int): the id of the class instance

        Methods:
            None:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """to initialize object instances"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        """To update arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To return dictionary containing attributes"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)
