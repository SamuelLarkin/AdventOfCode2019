#!/usr/bin/env  python3

import unittest

from interpreter import amplify



class TestDay07(unittest.TestCase):
    def test1(self):
        #from pudb import set_trace; set_trace()
        pgm = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        self.assertEqual(amplify(pgm, (4,3,2,1,0)), 43210)


    def test2(self):
        pgm = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        self.assertEqual(amplify(pgm, (0,1,2,3,4)), 54321)


    def test3(self):
        pgm = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        self.assertEqual(amplify(pgm, (1,0,4,3,2)), 65210)


    def test4(self):
        pgm = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        self.assertEqual(amplify(pgm, (9,8,7,6,5)), 139629729)


    def test5(self):
        pgm = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
        self.assertEqual(amplify(pgm, (9,7,8,5,6)), 18216)


