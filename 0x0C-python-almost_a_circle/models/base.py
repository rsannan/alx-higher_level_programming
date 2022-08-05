#!/usr/bin/python3
"""This module contains Base class definition"""


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
