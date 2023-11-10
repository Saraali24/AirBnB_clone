#!/usr/bin/python3
""" Testing for Review class"""

from models import *
import unittest
from datetime import datetime


class Test_Review(unittest.TestCase):
    """
    Testing for review class
    """

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

    def setUp(self):
        self.model = Review()
        self.model.save()


if __name__ == "__main__":
    unittest.main()
