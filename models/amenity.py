#!/usr/bin/python3
"""Make class Amenity inheret from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):

    """Amenity class definition
    Attributes:
        name (str): name of class
    """

    name = ""
