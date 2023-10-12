#!/usr/bin/env python3

import models
from models.base_model import BaseModel
import unittest
from datetime import datetime
import json
import uuid
import os


class TestBaseModel(unittest.TestCase):
    """test cases for the base model"""
    def __init__(self, *args, **kwargs):
        """initializing the init"""
        super().__init__(*args, **kwargs)

        self.name = "BaseModel"
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except PassTheError:
            pass

    def test_base_model_doctrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
