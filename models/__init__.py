#!/usr/bin/python3
"""__init__ method for models directory FileStorage"""
from models.engine.file_storage import FileStorage

def initialize_storage():
    storage = FileStorage()
    storage.reload()

if __name__ == "__main__":
    initialize_storage()
