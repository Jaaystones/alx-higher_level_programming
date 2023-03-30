#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):

    # Check if the list is empty
    if not list_of_integers:
        return None

    """peak to sorted values """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
