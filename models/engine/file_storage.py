#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage._objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage._objects[f"{obj_class_name}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = {key: obj.to_dict() for key, obj in FileStorage
                        ._objects.items()}
        with open(FileStorage._file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage._file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data.pop("__class__")
                    self.new(globals()[class_name](**obj_data))
        except FileNotFoundError:
            return
