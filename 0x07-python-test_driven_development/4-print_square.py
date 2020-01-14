#!/usr/bin/python3
def print_square(size):

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == int(size) and size < 0:
        raise TypeError("size must be an integer")
    elif size > 0:
        print(('#' * size + '\n') * size, end="")
