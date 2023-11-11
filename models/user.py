#!/usr/bin/python3
""" creating a user class from the base model """
from models.base_model import BaseModel


class User(BaseModel):
    """Class User def
    Attributes:
        email (str): email of user.
        password (str): The password of user.
        first_name (str): first name of user.
        last_name (str): last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
