#!/usr/bin/python3

def square(x):
    return x*x

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new = list(map(square, matrix[i]))
        new_matrix.append(new)
    return new_matrix
