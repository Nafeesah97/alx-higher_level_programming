#!/usr/bin/python3

"""
This module contains a class named rectangle
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

class Rectangle(Base):
    """
    A class named rectangle

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle
        x(int): 
        y(int):
    
    Methods:
        None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """To initialize class instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """To calculate area of rectangle"""
        return (self.__height * self.__width)
