#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods
for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing common attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    self.__dict__[key] = value
                else:
                    if key != "__class__":
                        self.__dict__[key] = value

    def __str__(self):
        """
        returns class name, id and the class dict
        """
        return (f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the updated_time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all the key and value
        of the instance
        """
        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()
        self.__dict__.update({"__class__": self.__class__.__name__})
        return self.__dict__
