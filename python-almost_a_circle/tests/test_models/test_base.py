#!/usr/bin/python3
'''
Tests for base model
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_as_positive(self):
        base = Base(72)
        self.assertEqual(base.id, 72)
        base = Base(87)
        self.assertEqual(base.id, 87)

    def test_id_as_negative(self):
        base = Base(-31)
        self.assertEqual(base.id, -31)
        base = Base(-16)
        self.assertEqual(base.id, -16)

    def test_id_as_none(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base(None)
        self.assertEqual(base.id, 2)

    def test_string_id(self):
        base = Base("Monty Python")
        self.assertEqual(base.id, "Monty Python")
        base = Base("Python is cool")
        self.assertEqual(base.id, "Python is cool")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 69}]), '[{"id": 69}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 54}]'), [{"id": 54}])


if __name__ == "__main__":
    unittest.main()
