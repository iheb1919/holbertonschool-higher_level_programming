#!/usr/bin/python3
"""
The example module supplies one function, print_sauare(size).  For example,

>>> print_sauare(5)
#####
#####
#####
#####
#####

"""


def print_square(size):
"""
return a sauare
"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == int(size) and size < 0:
        raise TypeError("size must be an integer")
    elif size > 0:
        print(('#' * size + '\n') * size, end="")


if __name__ == "__main__":
    import doctest.testfile("./tests/4-print_saquare.txt")
