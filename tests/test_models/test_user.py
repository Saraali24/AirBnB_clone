#!/usr/bin/python3
"""Testing for User class
Unittest classes:
    Test_User
"""

import unittest
from models import *
from datetime import datetime


class Test_User(unittest.TestCase):
    """
    Testing for user class
    """

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")

    def setUp(self):
        self.model = User()
        self.model.save()


if __name__ == "__main__":
    unittest.main()
