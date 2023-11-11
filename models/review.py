#!/usr/bin/python3
"""Make class Review inheret from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class def
    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): the review.
    """

    place_id = ""
    user_id = ""
    text = ""
