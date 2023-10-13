#!/usr/bin/env python3
"""model - test place"""

from models.place import Place
from tests.test_models.test_base_model import TestBaseModel

class TestPlace(TestBaseModel):
    """testing the place model"""


    def __init__(self, *args, **kwargs):
        """initialization"""

        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """testing if the city id is a str"""
        place = self.value()
        self.assertEqual(type(place.city_id), str)

    def test_user_id(self):
        """testing if the user id is a str"""
        place = self.value()
        self.assertEqual(type(place.user_id), str)

    def test_name(self):
        """testing is the name is a str"""
        place = self.value()
        self.assertEqual(type(place.name), str)
    
    def test_description(self):
        """testing if the desctiption is a string"""
        place = self.value()
        self.assertEqual(type(place.description), str)

    def test_number_rooms(self):
        """testing if the number of rooms is an int"""
        place = self.value()
        self.assertEqual(type(place.number_rooms), int)

    def test_number_bathrooms(self):
        """testing if the number of bathrooms is an int"""
        place = self.value()
        self.assertEqual(type(place.number_bathrooms), int)

    def test_max_guest(self):
        """testing is the max number of guests is an int"""
        place = self.value()
        self.assertEqual(type(place.max_guest), int)
    
    def test_price_by_night(self):
        """testing is the price by night is an int"""
        place = self.value()
        self.assertEqual(type(place.price_by_night), int)

    def test_latitude(self):
        """testing if the latitude is a float"""
        place = self.value()
        self.assertEqual(type(place.latitude), float)

    def test_longitude(self):
        """testing if the longitude is a float"""
        place =  self.value()
        self.assertEqual(type(place.longitude), float)

    def test_amenity_ids(self):
        """testing if the amenity ids are a list"""
        place = self.value()
        self.assertEqual(type(place.amenity_ids), list)
