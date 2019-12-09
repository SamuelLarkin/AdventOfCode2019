#!/usr/bin/env python3

import unittest

from solutions import ManhattonDistance
from solutions import Point
from solutions import minimumDistance
from solutions import parseInstructions
from solutions import parseSingleInstruction



class TestSolutions(unittest.TestCase):
    def testParseSingleInstruction(self):
        self.assertEqual(parseSingleInstruction('R75'), (75, 0))
        self.assertEqual(parseSingleInstruction('D30'), (0, -30))
        self.assertEqual(parseSingleInstruction('L12'), (-12, 0))
        self.assertEqual(parseSingleInstruction('U7'), (0, 7))


    def testParseInstruction(self):
        self.assertEqual(parseInstructions('R75,D30,R83,U83,L12,D49,R71,U7,L72'), [(75,0), (0,-30), (83,0), (0,83), (-12,0), (0,-49), (71,0), (0,7), (-72,0)])


    def testManhattanDistance(self):
        self.assertEqual(ManhattonDistance(Point(3, 3)), 6)
        self.assertEqual(ManhattonDistance(Point(-3, -3)), 6)
        self.assertEqual(ManhattonDistance(Point(3, 3), Point(-3, -3)), 12)
        self.assertEqual(ManhattonDistance(Point(5, 5), Point(5, 5)), 0)


    def test1(self):
        test = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
                  U62,R66,U55,R34,D71,R55,D58,R83'''.splitlines()
        wires = list(map(lambda l: parseInstructions(l), test))

        md, steps = minimumDistance(*wires)
        self.assertEqual(md, 159)
        self.assertEqual(steps, 610)


    def test1(self):
        test = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
                  U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''.splitlines()
        wires = list(map(lambda l: parseInstructions(l), test))

        md, steps = minimumDistance(*wires)
        self.assertEqual(md, 135)
        self.assertEqual(steps, 410)
