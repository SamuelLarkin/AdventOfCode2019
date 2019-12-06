#!/usr/bin/env  python3


import unittest
from solutions import crc
from solutions import crc3

class TestSolutions(unittest.TestCase):
    def testPartI(self):
        test = '''COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L'''.splitlines()
        self.assertEqual(crc(test), 42)

    def testPartII(self):
        test = '''COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L
        K)YOU
        I)SAN'''.splitlines()
        self.assertEqual(crc3(test), 4)
