#!/usr/bin/python3
"""This module contains Base class definition"""
import json

class Base:
    """This is the definition of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the Base object
            Args:
                id (int): the id of the object
        """
        Base.__nb_objects += 1
        self.id = id

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
        """ Returns the JSON representation of list_dictionaries
        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if (len(list_dictionaries) == 0 or
            list_dictionaries is None):
            return ('"[]"') 
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes list_objs to a text file, using a JSON representation
        Args:
            list_objs (list of instances who inherit of Base): object
            filename (str): filename
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as myfile:
            list_dict = [ele.to_dictionary() for ele in list_objs]
            myfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        if (json_string is None or
        len(json_string) == 0):
            return []
        
        """ Returns an object represented by a JSON string
        Args:
            my_str (str): JSON string
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of a class
            Args:
                dictionary (dict): double pointer to a dictionary
        
        """
        r1 = cls(1,1)
        r1.update(**dictionary)
        return r1
