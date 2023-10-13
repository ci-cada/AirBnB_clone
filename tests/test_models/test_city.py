#!/usr/bin/env python3
"""model - city test"""

from models.city import City
from tests.test_models.test_base_model import TestBaseModel

class TestCity(TestBaseModel):
    """testing the city model"""


    def __init__(self, *args, **kwargs):
        """initialization"""

        
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_city_name(self):
        """testing is the city name it a str"""
        city = self.value()
        self.assertEqual(type(city.name), str)

    def test_state_id(self):
        """testing if state id is a str"""
        city = self.value()
        self.assertEqual(type(city.state_id), str)
