#!/usr/bin/python3
""" among us """


def add_integer(a, b=98):
    """ adds integers """

    m = " must be an integer"

    if type(a) not in [int, float]:
        raise TypeError("a" + m)
    if type(b) not in [int, float]:
        raise TypeError("b" + m)

    va, vb = int(a), int(b)
    return va + vb
