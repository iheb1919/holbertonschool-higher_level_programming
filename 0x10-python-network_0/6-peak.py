#!/usr/bin/python3
"""
"""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    #print("lengh = {}".format(len(list_of_integers)))
    for i in range(1, len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
