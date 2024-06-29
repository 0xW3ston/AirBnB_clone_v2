#!/usr/bin/python3
""" document 0xw3ston """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ document 0xw3ston """

    def __init__(self, *args, **kwargs):
        """ document 0xw3ston """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ document 0xw3ston """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ document 0xw3ston """
        new = self.value()
        self.assertEqual(type(new.name), str)
