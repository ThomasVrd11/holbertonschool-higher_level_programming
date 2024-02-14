#!/usr/bin/python3
"""define function add_item"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

for argument in argv[1:]:
    my_list.append(argument)

save_to_json_file(my_list, filename)
