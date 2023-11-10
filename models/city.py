#!/usr/bin/python3
"""Make City class Inheret from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City """
    state_id = ""
    name = ""
