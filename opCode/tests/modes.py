#!/usr/bin/env  python3

import unittest

from interpreter import modes



class TestModes(unittest.TestCase):
    def test1(self):
        self.assertEqual(modes(1002), (2, 0, 1, 0))
        self.assertEqual(modes(1108), (8, 1, 1, 0))


    def test2(self):
        self.assertEqual(modes(21002), (2, 0, 1, 2))
        self.assertEqual(modes(11208), (8, 2, 1, 1))
