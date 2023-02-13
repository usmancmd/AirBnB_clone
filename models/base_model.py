#!/usr/bin/python3
"""Create class BaseModel that defines all
common attributes/methods for other classes"""


import datetime as dt
import json
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of the BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.today()
        self.updated_at = dt.datetime.today()

        if (kwargs is not None):
            for key, value in kwargs.items():
                if ((key == created_at) or (key == updated_at)):
                    self.__dict__[key] = dt.fromisoformat(value)
                    self.__dict__[key] = dt.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns an informal string representation"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, str(self.__dict__)))

    def save(self):
        """Updates attribute updated_at with the current datetime"""
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        copy_dict = dict(self.__dict__)  # Create copy of self.__dict__
        copy_dict["created_at"] = copy_dict["created_at"].isoformat()
        copy_dict["updated_at"] = copy_dict["updated_at"].isoformat()
        copy_dict["__class__"] = type(self).__name__
        return (copy_dict)
