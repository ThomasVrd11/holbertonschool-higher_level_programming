#!/usr/bin/python3
"""define function append_write"""


def append_write(filename="", text=""):
    """append write function"""
    with open(filename, "a", encoding="utf-8") as f:
        append_write = f.write(text)
        return append_write
