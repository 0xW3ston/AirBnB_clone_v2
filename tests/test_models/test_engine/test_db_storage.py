#!/usr/bin/python3
"""document 0xw3st"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage 0xw3st"
)
class test_DB_Storage(unittest.TestCase):
    """document 0xw3st"""

    def test_documentation(self):
        """document 0xw3st"""
        self.assertIsNot(DBStorage.__doc__, None)
