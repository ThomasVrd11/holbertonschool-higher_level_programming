#!/usr/bin/python3
"""Module for Base class"""
import json
from os import path


class Base:
    """A class to define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
            A function to initialize a Base object.

        Attributes:
            id (int): The id of the object.
            if id is not None, the id is set with this integer.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Description:
            A function to return the JSON string representation
            of list_dictionaries.

        Attributes:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            The JSON string representation of list_dictionaries. (str)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Description:
            A function to write the JSON string representation
            of list_objs to a file.

        Attributes:
            list_objs (list): A list of instances.

        Calls:
            to_json_string(list_dictionaries) : Calls the static method.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        list_dicts = []
        with open(filename, "w") as file:
            for i in list_objs:
                list_dicts.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Description:
            A function to return the list of the JSON string
            representation json_string.

        Attributes:
            json_string (str): A JSON string.

        Returns:
            The list of the JSON string representation json_string. (list)
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Description:
            A function to return an instance with all attributes
            already set.

        Attributes:
            **dictionary (dict): A dictionary of attributes.

        Returns:
            An instance with all attributes already set. (cls)
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """
        Description:
            A function to update the attributes of the object.
        """
        pass

    @classmethod
    def load_from_file(cls):
        """
        Description:
            A function to return a list of instances.

        Attributes:
            cls (class): The class of the object to return.
        """
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, "r") as file:
            obj = Base.from_json_string(file.read())
        list = [cls.create(**dict) for dict in obj]
        return list
