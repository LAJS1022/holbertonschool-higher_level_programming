#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([2, 7, 4, 6]), 7)

    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-8, -2, 0, 12]), 12)

    def test_single_element(self):
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        self.assertEqual(max_integer([-12, -3, -7, -9]), -3)

    def test_repeated_max(self):
        self.assertEqual(max_integer([5, 1, 5, 2]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([15, 10, 8, 2]), 15)

    def test_max_at_end(self):
        self.assertEqual(max_integer([4, 6, 2, 20]), 20)
