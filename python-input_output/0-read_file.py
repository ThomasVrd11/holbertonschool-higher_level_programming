#!/usr/bin/python3
"""define function read"""


def read_file(filename=""):
    """read file function"""
    with open(filename, encoding="utf-8") as f:
        f = (f.read()[:-1])
        if f == "":
            return
        else:
            print(f)
