#!/usr/bin/python3
"""define class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation of Student"""
        return self.__dict__
