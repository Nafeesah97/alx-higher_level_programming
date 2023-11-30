#!/usr/bin/python3
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    n = len(list_of_integers) / 2
    left = []
    append.left(list_of_integers[n])
    for i in range(len(list_of_integers)):
        if list_of_integers[n] < list_of_integers[i]:
            append.left(list_of_integers[i])
    find_peak(left)
