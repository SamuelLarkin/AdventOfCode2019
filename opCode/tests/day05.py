#!/usr/bin/env  python3

import unittest

from interpreter import Interpreter
from parser import parse



class TestInterpreter(unittest.TestCase):
    def test1(self):
        pgm = parse('3,9,8,9,10,9,4,9,99,-1,8')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(7))), 0)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(8))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(9))), 0)


    def test2(self):
        pgm = parse('3,9,7,9,10,9,4,9,99,-1,8')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(7))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(8))), 0)


    def test3(self):
        pgm = parse('3,3,1108,-1,8,3,4,3,99')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(7))), 0)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(8))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(9))), 0)


    def test4(self):
        pgm = parse('3,3,1107,-1,8,3,4,3,99')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(7))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(8))), 0)


    def test5(self):
        pgm = parse('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(0))), 0)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(1))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(2))), 1)


    def test6(self):
        pgm = parse('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(0))), 0)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(1))), 1)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(2))), 1)


    def test7(self):
        pgm = parse('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(7))), 999)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(8))), 1000)
        self.assertEqual(next(iter(Interpreter(pgm).giveInput(9))), 1001)
