#!/usr/bin/python3
"""
Testing City class
Unittest classes:
    Test_CityModel
"""
import unittest
from models.city import City
from datetime import datetime


class Test_CityModel(unittest.TestCase):
    """
    Testing for city class
    """

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")

    def setUp(self):
        self.model = City()
        self.model.save()


if __name__ == "__main__":
    unittest.main()
