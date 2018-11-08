"""
@author: Kudzai Tsapo (kudzai@charteredsys.com)

Description: 
--------------
This file contains the model classes for the Object Relational Mapper (Custom made)
"""

class Field:
    def __set__(self, obj, value):
        obj._data[self._name] = value

    def __get__(self, obj, type=None):
        return obj._data[self._name]

class Meta(type):
    def __new__(cls, name, bases, attrs):
        for field_name, field in attrs.items():
            pass