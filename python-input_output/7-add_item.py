#!/usr/bin/python3
"""define function add_item"""
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """function that adds all arguments to a Python list"""
    try:
        my_list = load(add_item.json)
    except BaseException:
        my_list = []

    my_list += args
    save(my_list, add_item.json)


args = sys.argv[1:]
add_item(args)
