#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
