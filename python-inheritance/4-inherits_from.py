#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from"""

    return issubclass(type(obj), a_class) and not isinstance(obj, a_class)
