#!/usr/bin/python3
"""define class Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of Student"""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
