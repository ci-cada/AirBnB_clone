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

    def test_id(self):
        """test to show if a new id has been created"""
        Bm = BaseModel()
        Bm2 = BaseModel()
        self.assertNotEqual(Bm.id, Bm2.id)

    def test_basemodel_to_dict(self):
        BaseModel_dict = BaseModel.to_dict()
        self.assertIsInstance(BaseModel_dict, dict)
        self.assertEqual(BaseModel_dict["id"], BaseModel.id)
        self.assertEqual(BaseModel_dict["__class__"], "BaseModel")
        self.assertEqual(BaseModel_dict["created_at"],
                         BaseModel.created_at.isoformat())
        self.assertEqual(BaseModel_dict["updated_at"],
                         BaseModel.updated_at.isoformat())

    def test_base_model_str(self):
        self.assertEqual(str(BaseModel), "[BaseModel] ({}) {}".
                         format(BaseModel.id, BaseModel.__dict__))

    def test_basemodel_save(self):
        created_at = BaseModel.created_at
        BaseModel.save()
        self.assertEqual(BaseModel.created_at, created_at)
        self.assertNotEqual(BaseModel.updated_at, created_at)

    def test_Isinstance(self):
        Bm = BaseModel
        self.assertIsInstance(Bm, BaseModel)
        self.assertIsInstance(Bm.id, self)
        self.assertIsInstance(Bm.created_at, datetime)
        self.assertIsInstance(Bm.updated_at, datetime)

    def test_Instantation_kwags(self):
        Bm_dict = ({'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298', 'updated_at':
                    '2017-09-28T21:03:54.052298'})
        Bm = BaseModel(**Bm_dict)
        self.assertIsInstance(Bm, BaseModel)
        self.assertEqual(Bm.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(Bm.created_at,
                         datetime.
                         strptime("2017-09-28T21:03:54.052298",
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(Bm.updated_at,
                         datetime.
                         strptime("2017-09-28T21:03:54.052298",
                                  '%Y-%m-%dT%H:%M:%S.%f'))


if __name__ == '__main__':
    unittest.main()
