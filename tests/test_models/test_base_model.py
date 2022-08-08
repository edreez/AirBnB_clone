#!/usr/bin/python3
"""
This file is the unit test for the base model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    unit test for base model
    """
    bm = BaseModel()

    def test_init(self):
        """
        test the class init method
        """

        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        """
        testing the output of the class
        """

        self.assertEqual(self.bm.__class__.__name__, "BaseModel")

    def test_save(self):
        """
        testing save method
        """

        self.assertEqual(self.bm.created_at, self.bm.updated_at)
        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_to_dict(self):
        """
        testing to_dict method
        """

        self.bm.to_dict()
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, str)
        self.assertIsInstance(self.bm.updated_at, str)


if __name__ == "__main__":
    unittest.main()
