#!/usr/bin/python3
"""function find_peak """
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return (list_of_integers[0])
    if length == 2:
        return max(list_of_integers)
    if length % 2 == 0:
        n = int(length / 2)
    else:
        n = int((length + 1)/2)
    left = []
    left.append(list_of_integers[n])
    for i in range(len(list_of_integers)):
        if list_of_integers[n] < list_of_integers[i]:
            left.append(list_of_integers[i])
    return find_peak(left)
