#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if j < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
            j += 1
    if not i:
        print("")
