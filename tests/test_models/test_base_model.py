#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes_initialization(self):
        # Check if the ID is a valid UUID
        self.assertTrue(uuid.UUID(self.base_model.id))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
