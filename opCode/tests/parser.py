#!/usr/bin/env  python3

import unittest

from parser import parse



class TestParser(unittest.TestCase):
    def test1(self):
        self.assertEqual(parse('3,9,8,9,10,9,4,9,99,-1,8'), [3,9,8,9,10,9,4,9,99,-1,8])
