#!/usr/bin/env  python3

import unittest

from parser import parse


class TestParser(unittest.TestCase):
    def test1(self):
        data = '''<x=-4, y=3, z=15>
        <x=-11, y=-10, z=13>
        <x=2, y=2, z=18>
        <x=7, y=-1, z=0>'''.splitlines()
        planets = parse(data)
        self.assertEqual(planets.tolist(), [[-4, 3, 15], [-11, -10, 13], [2, 2, 18], [7, -1, 0]])
