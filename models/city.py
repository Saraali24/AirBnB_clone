#!/usr/bin/python3
"""Make City class Inheret from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City
    Attributes:
        state_id (str): state id.
        name (str): name of  city.
    """

    state_id = ""
    name = ""
