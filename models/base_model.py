#!/usr/bin/python3

"""BaseModel the parent class """
from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """Define BaseModel class """

    def __init__(self, *args, **kwargs):
        """Initialize new objects """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Print str representation of object """

        new = (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
        return new

    def save(self):
        """Update object's updates_at with current time """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return __dict__ of object"""

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
