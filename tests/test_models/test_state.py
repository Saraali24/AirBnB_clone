#!/usr/bin/python3
""" Testing for State class
Unittest classes:
    Test_State
"""

from datetime import datetime
from models import *
import unittest


class Test_State(unittest.TestCase):
    """
    Testing for state class
    """

    def test_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")

    def setUp(self):
        self.model = State()
        self.model.save()


if __name__ == "__main__":
    unittest.main()
