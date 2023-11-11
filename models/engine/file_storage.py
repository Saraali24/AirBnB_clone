#!/usr/bin/python3
"""FileStorage class def."""

import os
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place


class FileStorage:
    """Class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Make an instance in objetcs dictionary"""
        cls_name = obj.__class__.__name__
        key_dictionary = "{}.{}".format(cls_name, obj.id)
        FileStorage.__objects[key_dictionary] = obj

    def save(self):
        """serelization of objects into JSON file"""
        str_serialized = {}

        for key_dictionary, obj in FileStorage.__objects.items():
            str_serialized[key_dictionary] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as j_file:
            json.dump(str_serialized, j_file)

    def reload(self):
        """Deserelization into objects"""

        if os.path.exists(FileStorage.__file_path):

            with open(FileStorage.__file_path, 'r') as file:

                try:
                    str_serialized = json.load(file)

                    for key_dictionary, objct_dict in str_serialized.items():
                        cls_name = objct_dict.pop("__class__", None)

                        if cls_name:
                            objct_id = key_dictionary.split('.')[1]
                            class_s = getattr(models, cls_name)
                            obj = class_s(**objct_dict)
                            FileStorage.__objects[key_dictionary] = obj

                except FileNotFoundError:
                    pass
