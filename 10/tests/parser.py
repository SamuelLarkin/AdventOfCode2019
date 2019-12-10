#!/usr/bin/env  python3

import unittest

from parser import parse
from parser import Position


class TestParser(unittest.TestCase):
    def test1(self):
        data = '''.#..#
        .....
        #####
        ....#
        ...##'''.splitlines()
        asteroids = parse(data)
        self.assertEqual(asteroids, (Position(x=1, y=0),
        Position(x=4, y=0),
        Position(x=0, y=2),
        Position(x=1, y=2),
        Position(x=2, y=2),
        Position(x=3, y=2),
        Position(x=4, y=2),
        Position(x=4, y=3),
        Position(x=3, y=4),
        Position(x=4, y=4)))

