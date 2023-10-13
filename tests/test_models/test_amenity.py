#!/usr/bin/env python3
"""model - test amenity"""

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel

class TestAmenity(TestBaseModel):
    """testing the amenity model"""

    
    def __init__(self, *args, **kwargs):
        """init function"""

        super().__init__(*args,**kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """testing if amenity name is a str"""
        amenity = self.value()
        self.assertEqual(type(amenity.name), str)