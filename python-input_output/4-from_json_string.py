#!/usr/bin/python3
"""define function from_json_string"""

import json


def from_json_string(my_str):
    """return object represented by JSON string"""
    return json.loads(my_str)
