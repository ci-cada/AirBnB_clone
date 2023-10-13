#!/usr/bin/env python3
"""model - review test"""

from models.review import Review
from tests.test_models.test_base_model import TestBaseModel

class TestReview(TestBaseModel):
    """testing the review model"""


    def __init__(self, *args, **kwargs):
        """initialization"""

        
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """testing is the place id in the review is a str"""
        review = self.value()
        self.assertEqual(type(review.place_id), str)

    def test_user_id(self):
        """testing if user id in review is a str"""
        review = self.value()
        self.assertEqual(type(review.user_id), str)

    def test_text(self):
        """testing if the text in review is a string"""
        review = self.value()
        self.assertEqual(type(review.text), str)
