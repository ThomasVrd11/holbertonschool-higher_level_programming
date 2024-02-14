#!/usr/bin/python3
"""define function open write"""


def write_file(filename="", text=""):
    """write file function"""
    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
