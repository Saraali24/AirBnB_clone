#!/usr/bin/python3
from models import *
import unittest
from datetime import datetime


class Test_AmenityClass(unittest.TestCase):
    """
    Test Amenity Class
    """

    def Set_up(self):
        self.model = Amenity()
        self.model.save()

    def Test_Initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
