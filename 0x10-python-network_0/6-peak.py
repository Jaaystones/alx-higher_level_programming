#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    mid_i = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_i = mid_i // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_i // 2 == 0:
                mid_i = 2
            mid = mid + mid_i // 2
        elif mid_i > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_i // 2 == 0:
                mid_i = 2
            mid = mid - mid_i // 2
        else:
            return list_of_integers[mid]
