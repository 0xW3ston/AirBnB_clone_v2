#!/usr/bin/python3
""" Module for testing file 0xw3st storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db",
    "Test is not re 0xw3st for fileStorage"
)
class test_file_Storage(unittest.TestCase):
    """Class to test the FileStorage 0xw3st method"""

    def setUp(self):
        """set up test env 0xw3st"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at end of tests 0xw3st"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty 0xw3st"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to 0xw3st's objects"""
        new = BaseModel()
        temp = None
        obj = None
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """__objects is properly 0xw3st"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel 0xw3st save"""
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_empty(self):
        """Data is saved to 0xw3st file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_save(self):
        """FileStorage save 0xw3st method"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Storage file is successfully 0xw3ston loaded to __objects"""
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    def test_reload_empty(self):
        """Load from an empty 0xw3ston file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens 0xw3ston if file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """BaseModel save method calls storage save 0xw3ston"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_type_path(self):
        """Confirm __file_path is string 0xw3ston"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict 0xw3ston"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Key is properly formatted 0xw3ston"""
        new = BaseModel()
        new.save()
        _id = new.to_dict()["id"]
        temp = None
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, "BaseModel" + "." + _id)

    def test_storage_var_created(self):
        """FileStorage object storage 0xw3ston created_at"""
        from models.engine.file_storage import FileStorage

        self.assertEqual(type(storage), FileStorage)
