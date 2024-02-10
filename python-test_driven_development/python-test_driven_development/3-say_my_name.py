#!/usr/bin/python3
"""define function say my name"""


def say_my_name(first_name, last_name=""):
    """function say my name"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
    