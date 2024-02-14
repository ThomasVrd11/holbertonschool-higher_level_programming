#!/usr/bin/python3
"""defining a class MyList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
