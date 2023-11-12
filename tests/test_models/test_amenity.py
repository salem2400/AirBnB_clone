#!/usr/bin/python3

"""Unittest module for the Amenity Class."""

import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import storage
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity_instance = Amenity()
        self.assertEqual(str(type(amenity_instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, 'testme'))
        self.assertEqual(type(getattr(amenity_instance, 'testme', None)), str)

if __name__ == "__main__":
    unittest.main()
