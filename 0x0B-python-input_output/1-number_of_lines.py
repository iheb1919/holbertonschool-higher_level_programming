#!/usr/bin/python3
"""
1-number_of_lines
"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file.
    """
    with open(filename, 'r') as f:
        line = 0
        for i in f:
            line += 1
        return(line)
