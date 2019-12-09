#!/usr/bin/env  python3

import unittest

from solutions import parse_input
from solutions import process
from solutions import modes



class TestSolutions(unittest.TestCase):
    def testParseInput(self):
        self.assertEqual(parse_input('3,9,8,9,10,9,4,9,99,-1,8'), [3,9,8,9,10,9,4,9,99,-1,8])


    def testModes(self):
        self.assertEqual(modes(1002), (2, 0, 1, 0))
        self.assertEqual(modes(1108), (8, 1, 1, 0))
        with self.assertRaises(AssertionError):
            self.assertEqual(modes(11108), (8, 1, 1, 1))


    def test1(self):
        test = parse_input('3,9,8,9,10,9,4,9,99,-1,8')
        self.assertEqual(process(test, 7), 0)
        self.assertEqual(process(test, 8), 1)
        self.assertEqual(process(test, 9), 0)


    def test2(self):
        test = parse_input('3,9,7,9,10,9,4,9,99,-1,8')
        self.assertEqual(process(test, 7), 1)
        self.assertEqual(process(test, 8), 0)


    def test3(self):
        test = parse_input('3,3,1108,-1,8,3,4,3,99')
        self.assertEqual(process(test, 7), 0)
        self.assertEqual(process(test, 8), 1)
        self.assertEqual(process(test, 9), 0)


    def test4(self):
        test = parse_input('3,3,1107,-1,8,3,4,3,99')
        self.assertEqual(process(test, 7), 1)
        self.assertEqual(process(test, 8), 0)


    def test5(self):
        test = parse_input('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        self.assertEqual(process(test, 0), 0)
        self.assertEqual(process(test, 1), 1)
        self.assertEqual(process(test, 2), 1)


    def test6(self):
        test = parse_input('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        self.assertEqual(process(test, 0), 0)
        self.assertEqual(process(test, 1), 1)
        self.assertEqual(process(test, 2), 1)


    def test7(self):
        test = parse_input('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
        self.assertEqual(process(test, 7), 999)
        self.assertEqual(process(test, 8), 1000)
        self.assertEqual(process(test, 9), 1001)
