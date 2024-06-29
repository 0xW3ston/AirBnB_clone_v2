#!/usr/bin/python3
""" document 0xw3ston """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ document 0xw3ston """

    def __init__(self, *args, **kwargs):
        """ document 0xw3ston """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ document 0xw3ston """
        new = self.value()
        self.assertEqual(type(new.name), str)
