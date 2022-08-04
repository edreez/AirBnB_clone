#!/usr/bin/python3
"""
This file is the unit test for the base model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        bm = BaseModel()

        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        bm = BaseModel()

        self.assertEqual(bm.__class__.__name__, "BaseModel")

    def test_save(self):
        bm = BaseModel()
        self.assertEqual(bm.created_at, bm.updated_at)
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        bm = BaseModel()
        bm.to_dict()

        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, str)
        self.assertIsInstance(bm.updated_at, str)


if __name__ == "__main__":
    unittest.main()
