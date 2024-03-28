#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
import datetime
import json
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up a clean environment before each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_default(self):
        """Test creating a BaseModel instance with default values"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test creating a BaseModel instance with keyword arguments"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test creating a BaseModel instance with non-string keys in kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test saving BaseModel instance to JSON file"""
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation of BaseModel instance"""
        i = BaseModel()
        self.assertEqual(
            str(i),
            "[{}] ({}) {}".format("BaseModel", i.id, i.__dict__)
        )

    def test_todict(self):
        """Test converting BaseModel instance to dictionary"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test creating a BaseModel instance with kwargs containing None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test a BaseModel instance containing a single non-id key"""
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """Test ID attribute of BaseModel instance"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute of BaseModel instance"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute of BaseModel instance"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
