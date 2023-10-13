#!/usr/bin/env python3
"""model - user test"""

from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """testing the user model"""

    def __init__(self, *args, **kwargs):
        """initialization"""

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """testing if the first name is a string"""
        User = self.value
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """testing if the last name is a str"""
        User = self.value
        self.assertEqual(type(User.last_name), str)

    def test_password(self):
        """testing if the password is a str"""
        User = self.value
        self.assertEqual(type(User.password), str)

    def test_email(self):
        User = self.value
        self.assertEqual(type(User.email), str)
