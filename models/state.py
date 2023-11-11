#!/usr/bin/python3
"""Make class State inheret from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """Define class State
    Attributes:
        name (str): The name.
    """

    name = ""
