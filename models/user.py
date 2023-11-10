#!/usr/bin/python3
""" creating a user class from the base model """
from models.base_model import BaseModel


class User(BaseModel):
    """Class User def."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
