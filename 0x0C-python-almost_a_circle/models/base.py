#!/usr/bin/python3
"""to serialise/deserialise"""
import json
import os
"""
This module contains the class base that
is used to instantiate the id
Author: Nafeesah
"""


class Base:
    """
    This is class named Base.

    Attributes:
        nb_objects(int): number of instances
        id(int): id of class instances

    Methods:
        None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """To instantiate object attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        objects_to_json = [obj.to_dictionary() for obj in list_objs]
    
        with open(filename, "w") as file:
            file.write(cls.to_json_string(objects_to_json))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            string_data = []
        else:
            string_data = json.loads(json_string)
        return string_data

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if issubclass(cls, Base):
            if cls.__name__ == "Base":
                return Base(dictionary.get("id", None))

            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        output = []
        file_path = f"{cls.__name__}.json"
        if not os.path.exists(file_path):
            return output

        with open(f"{cls.__name__}.json", "r") as f:
            json_data = f.read()
            json_dic = cls.from_json_string(json_data)
            for i in json_dic:
                output.append(cls.create(**i))
        return output
