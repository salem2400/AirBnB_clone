#!/usr/bin/python3
"""Module for the FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class to manage serialization and deserialization of instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: value.to_dict() for key, value in self.__class__.__objects.items()}
        with open(self.__class__.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__class__.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                self.__class__.__objects = {
                    f"{cls_name}.{obj_id}": cls(**value)
                    for cls_name, obj_id, cls, value in
                    (key.split('.') + (cls, value) for key, (cls_name, obj_id, cls, value) in obj_dict.items())
                }
        except FileNotFoundError:
            pass
