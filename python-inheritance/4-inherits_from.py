#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from"""

    return isinstance(obj, a_class) and type(obj) is not a_class
