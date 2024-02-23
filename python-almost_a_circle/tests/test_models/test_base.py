#!/usr/bin/python3
"""Tests for the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_assign_id(self):  # Check if id is assigned correctly
        test0 = Base(3)
        self.assertEqual(test0.id, 3)

    def test_no_id_assigned(self):  # Test if id not assigned (default = 1)
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base()  # previous id = 1, new id = 2
        self.assertEqual(test2.id, 2)

    def test_to_json_string_none(self):  # Test to_json_string method with None
        self.assertEqual(Base.to_json_string(None), '[]')

    # Test to_json_string method with empty list
    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    # Test to_json_string method with list of dictionaries
    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    # Test from_json_string method with None
    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    # Test from_json_string method with empty string
    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    # Test from_json_string method with list of dictionaries
    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
