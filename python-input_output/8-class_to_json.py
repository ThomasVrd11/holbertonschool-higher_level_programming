#!/usr/bin/python3
"""define function class_to_json"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
