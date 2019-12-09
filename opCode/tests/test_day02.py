#!/usr/bin/env python3

import unittest

from solutions import parse
from solutions import process


class TestSolutions(unittest.TestCase):
    def testParse(self):
        self.assertEqual(parse('1,9,10,3,2,3,11,0,99,30,40,50'), [1,9,10,3,2,3,11,0,99,30,40,50])


    def testProcess(self):
        data = parse('1,9,10,3,2,3,11,0,99,30,40,50')
        self.assertEqual(process(data), (3500, 9, 10))
