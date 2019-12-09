#!/usr/bin/env  python3


import unittest

from interpreter import Interpreter
from parser import parse



class TestDay09(unittest.TestCase):
    def test1(self):
        """
        Takes no input and produces a copy of itself as output.
        """
        pgm = parse('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        interpreter = Interpreter(pgm)
        #import pudb; pudb.set_trace()
        #self.assertEqual(interpreter(), [])
        self.assertEqual(interpreter.diagnostic(), [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])


    def test2(self):
        """
        Should output a 16-digit number.
        """
        pgm = parse('1102,34915192,34915192,7,4,7,99,0')
        interpreter = Interpreter(pgm)
        self.assertEqual(interpreter(), 1219070632396864)


    def test3(self):
        """
        Should output the large number in the middle.
        """
        pgm = parse('104,1125899906842624,99')
        interpreter = Interpreter(pgm)
        self.assertEqual(interpreter(), 1125899906842624)


