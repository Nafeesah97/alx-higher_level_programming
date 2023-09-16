#!/usr/bin/python3

"""
This module contains function for pascal triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascals triangle"""
    res = []
    for i in range(n):
        p = []
        for j in range(i + 1):
            if j == 0 or j == i:
                p.append(1)
            else:
                previous_row = res[i - 1]
                p.append(previous_row[j - 1] + previous_row[j])
        res.append(p)
    return res
