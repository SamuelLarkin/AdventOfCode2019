#!/usr/bin/env python3

import unittest

from solutions import hasAPairOfDigits
from solutions import increasing
from solutions import toTuple
from solutions import twoDigits


class TestSolutions(unittest.TestCase):
    def testToTuple(self):
        self.assertEqual(toTuple(147223), (1,4,7,2,2,3))


    def testTwoDigits(self):
        self.assertTrue(twoDigits(toTuple(123446)))
        self.assertFalse(twoDigits(toTuple(123789)))


    def testIncreasing(self):
        self.assertTrue(increasing(toTuple(123446)))
        self.assertFalse(increasing(toTuple(123441)))
        self.assertFalse(increasing(toTuple(706948)))


    def testSoltionPartI(self):
        self.assertEqual(list(filter(increasing, filter(twoDigits, map(toTuple, [111111])))), [(1, 1, 1, 1, 1, 1)])
        self.assertEqual(list(filter(increasing, filter(twoDigits, map(toTuple, [223450])))), [])
        self.assertEqual(list(filter(increasing, filter(twoDigits, map(toTuple, [123789])))), [])


    def testSoltionPartII(self):
        self.assertEqual(list(filter(hasAPairOfDigits, filter(increasing, filter(twoDigits, map(toTuple, [112233]))))), [(1, 1, 2, 2, 3, 3)])
        self.assertEqual(list(filter(hasAPairOfDigits, filter(increasing, filter(twoDigits, map(toTuple, [123444]))))), [])
        self.assertEqual(list(filter(hasAPairOfDigits, filter(increasing, filter(twoDigits, map(toTuple, [111122]))))), [(1, 1, 1, 1, 2, 2)])

