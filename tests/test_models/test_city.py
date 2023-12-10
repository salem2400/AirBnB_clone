#!/usr/bin/python3
"""
Test City class
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """
    Test the City class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test the state_id attribute
        """
        new_city = self.value()
        self.assertEqual(type(new_city.state_id), str)

    def test_name(self):
        """
        Test the name attribute
        """
        new_city = self.value()
        self.assertEqual(type(new_city.name), str)
