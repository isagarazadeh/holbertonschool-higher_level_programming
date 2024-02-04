#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([516, 25, 76, 31]), 516)
        self.assertEqual(max_integer([4, 100, 44, 5]), 100)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-71, -31, -53, -66]), -31)
        self.assertEqual(max_integer([-51, -31, -46, -72]), -31)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([57, 72, 13, -44]), 72)
        self.assertEqual(max_integer([-156, 248, -13, 754]), 754)

    def test_one_element(self):
        self.assertEqual(max_integer([-5]), -5)
