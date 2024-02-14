#!/usr/bin/python3
"""define function to_json_string"""

import json


def to_json_string(my_obj):
    """return JSON representation of an object"""
    return json.dumps(my_obj)
