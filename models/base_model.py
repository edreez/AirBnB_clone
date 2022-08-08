#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods
for other classes
"""
import uuid
from datetime import datetime
from models import storage


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
            storage.new(self)
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
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datemtimes converted to strings
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
