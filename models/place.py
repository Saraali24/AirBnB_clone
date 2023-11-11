#!/usr/bin/python3
"""Make class Place inheret from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place definition
    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): The name.
        description (str): The description.
        number_rooms (int): number of rooms.
        number_bathrooms (int): The num of bathrooms.
        max_guest (int): The max num of guests.
        price_by_night (int):  price of place.
        latitude (float): lat of place.
        longitude (float): longit of  place.
        amenity_ids (list): A list of  ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
