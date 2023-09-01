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
        my_print(): prints in stdout the square with the character #

    Example:
        >>> my_square = Square(90)

    """
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """
        to get position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        To set position value

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        finds area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square wiith a character #

        """
        if (self.__size == 0):
            print()

        for _ in range(self.__position[1]):
            print()

        i = 0
        while i < self.__size:
            print(" " * self.__position[0] + "#" * self.__size)
            i += 1
