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
    if (
            not isinstance(matrix, list)
            or not all(isinstance(sublist, list) for sublist in matrix)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    num_columns = len(matrix[0])
    if not all(len(sublist) == num_columns for sublist in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (
            not all(
                isinstance(
                    element, (int, float)
                    ) for row in matrix for element in row
            )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
