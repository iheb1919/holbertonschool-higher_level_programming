#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer(). For example,

>>> add_integer(1,2)
3
"""




def add_integer(a, b=98):

    """ Returns the sum of 2 parameters. """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a = int(a)
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    elif type(b) == float:
        b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
