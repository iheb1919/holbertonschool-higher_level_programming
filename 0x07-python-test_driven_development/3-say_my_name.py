#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    first = False
    last = False
    if first_name is None and last_name is None:
        raise TypeError("missing 1 required positional argument: 'first_name'")
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is " + first_name + " " + last_name)
