#!/usr/bin/env python3

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel for the Airbnb_Clone project."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs (dict): Key/value pairs of attributes.

        Attributes:
        - id: A unique Identifier for each instance.
        - created_at: The timestamp when the instance is created.
        - updated_at: The timestamp when the instance is last updated.
        
        """
        if kwargs:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(kwargs.get('created_at'), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs.get('updated_at'), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
            models.storage.new(self)

    def save(self):
        """
        Update the 'updated_at' attribute with
        the current datetime and save it to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key in ["created_at", "updated_at"]:
            new_dict[key] = new_dict[key].isoformat()
        return new_dict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
