#!/usr/bin/python3

"""
This module contains mathematical operation
The operation is division
Author: Nafeesah
"""

def matrix_divided(matrix, div):
    """
    This function divides all element of a matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for sublist in matrix:
        if not isinstance(sublist, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for sublist in matrix:
        num_columns = len(matrix[0])
        if not (len(sublist) == num_columns):
            raise TypeError("Each row of the matrix must have the same size")
    for sublist in matrix:
        for element in sublist:
            if not (isinstance(element (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    inner = []
    new = []

    for element in sublist:
        inner.append(round(element/div, 2))
    new.append(inner)

    return new
