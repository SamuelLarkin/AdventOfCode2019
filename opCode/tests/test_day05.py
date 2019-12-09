#!/usr/bin/env  python3

import unittest

from parser import parse
from interpreter import Interpreter
from interpreter import modes



class TestParser(unittest.TestCase):
    def test1(self):
        self.assertEqual(parse('3,9,8,9,10,9,4,9,99,-1,8'), [3,9,8,9,10,9,4,9,99,-1,8])



class TestModes(unittest.TestCase):
    def test1(self):
        self.assertEqual(modes(1002), (2, 0, 1, 0))
        self.assertEqual(modes(1108), (8, 1, 1, 0))


    def test2(self):
        self.assertEqual(modes(21002), (2, 0, 1, 2))
        self.assertEqual(modes(11208), (8, 2, 1, 1))



class TestInterpreter(unittest.TestCase):
    def test1(self):
        pgm = parse('3,9,8,9,10,9,4,9,99,-1,8')
        self.assertEqual(Interpreter(pgm, 7)(), 0)
        self.assertEqual(Interpreter(pgm, 8)(), 1)
        self.assertEqual(Interpreter(pgm, 9)(), 0)


    def test2(self):
        pgm = parse('3,9,7,9,10,9,4,9,99,-1,8')
        self.assertEqual(Interpreter(pgm, 7)(), 1)
        self.assertEqual(Interpreter(pgm, 8)(), 0)


    def test3(self):
        pgm = parse('3,3,1108,-1,8,3,4,3,99')
        self.assertEqual(Interpreter(pgm, 7)(), 0)
        self.assertEqual(Interpreter(pgm, 8)(), 1)
        self.assertEqual(Interpreter(pgm, 9)(), 0)


    def test4(self):
        pgm = parse('3,3,1107,-1,8,3,4,3,99')
        self.assertEqual(Interpreter(pgm, 7)(), 1)
        self.assertEqual(Interpreter(pgm, 8)(), 0)


    def test5(self):
        pgm = parse('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        self.assertEqual(Interpreter(pgm, 0)(), 0)
        self.assertEqual(Interpreter(pgm, 1)(), 1)
        self.assertEqual(Interpreter(pgm, 2)(), 1)


    def test6(self):
        pgm = parse('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        self.assertEqual(Interpreter(pgm, 0)(), 0)
        self.assertEqual(Interpreter(pgm, 1)(), 1)
        self.assertEqual(Interpreter(pgm, 2)(), 1)


    def test7(self):
        pgm = parse('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
        self.assertEqual(Interpreter(pgm, 7)(), 999)
        self.assertEqual(Interpreter(pgm, 8)(), 1000)
        self.assertEqual(Interpreter(pgm, 9)(), 1001)
