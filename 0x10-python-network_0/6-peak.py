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
    n = int(length // 2)

    if n < length - 1 and list_of_integers[n] >= list_of_integers[n + 1] and \
            list_of_integers[n] >= list_of_integers[n - 1]:
        return list_of_integers[n]
    if n < length - 1 and list_of_integers[n] < \
            list_of_integers[n + 1]:
        return find_peak(list_of_integers[(n + 1):])
    if n > 0 and list_of_integers[n] < \
            list_of_integers[n - 1]:
        return find_peak(list_of_integers[:n])
