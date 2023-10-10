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