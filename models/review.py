#!/usr/bin/python3
"""Make class Review inheret from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class def."""
    place_id = ""
    user_id = ""
    text = ""
