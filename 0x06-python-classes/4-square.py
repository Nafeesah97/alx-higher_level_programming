#!/usr/bin/python3

"""

This module defines a square

"""


class Square(object):
    """
    It defines the class of square

    Attributes:
        size (int): the size of one side of the square

    Methods:
        area(): returns the current square area

    Example:
        >>> my_square = Square(90)

    """
    def __init__(self, size=0):
        """
        initializes a square instance.

        Args:
            size (int): the sizeof the square. default is 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        to get private instance size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size to a new size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        finds area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2
