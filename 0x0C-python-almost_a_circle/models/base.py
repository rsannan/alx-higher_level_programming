#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the Base object
            Args:
                id (int): the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None:
            self.__id = value
        else:
            self.__id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes list_objs to a text file, using a JSON representation

        Args:
            list_objs (list of instances who inherit of Base): object
            filename (str): filename
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dict = [ele.to_dictionary() for ele in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns an object represented by a JSON string

        Args:
            my_str (str): JSON string
        """
        if (json_string is None or
           len(json_string) == 0):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of a class
            Args:
                dictionary (dict): double pointer to a dictionary

        """
        r1 = cls(1, 1)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """returns a list of instances of current
        class using the method
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as myfile:
                inst_list_dict = cls.from_json_string(myfile.read())
                return [cls.create(**ele) for ele in inst_list_dict]
        except FileNotFoundError:
            return []
