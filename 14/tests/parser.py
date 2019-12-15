#!/usr/bin/env  python3

import unittest

from parser import Reaction
from parser import distance
from parser import parse
from parser import subparse



class TestSubparse(unittest.TestCase):
    def test1(self):
        self.assertEqual(subparse('1 A'), (1, 'A'))


    def test2(self):
        self.assertEqual(subparse('1 ABC'), (1, 'ABC'))



class TestParse(unittest.TestCase):
    def test1(self):
        data = '''10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL'''.splitlines()
        reactions = parse(data)
        self.assertEqual(reactions, {
            'ORE': Reaction(quantity=0, compound='ORE', reactants={}, distance=0),
            'A': Reaction(quantity=10, compound='A', reactants={'ORE': 10}, distance=1),
            'B': Reaction(quantity=1, compound='B', reactants={'ORE': 1}, distance=1),
            'C': Reaction(quantity=1, compound='C', reactants={'A': 7, 'B': 1}, distance=2),
            'D': Reaction(quantity=1, compound='D', reactants={'A': 7, 'C': 1}, distance=3),
            'E': Reaction(quantity=1, compound='E', reactants={'A': 7, 'D': 1}, distance=4),
            'FUEL': Reaction(quantity=1, compound='FUEL', reactants={'A': 7, 'E': 1}, distance=5),
            })



class TestDistance(unittest.TestCase):
    def setUp(self):
        data = '''10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL'''.splitlines()
        self.reactions = { k: v._replace(distance=None) for k, v in parse(data).items() }
        self.reactions['ORE'] = self.reactions['ORE']._replace(distance=0)


    def test0(self):
        d = distance('ORE', self.reactions)
        self.assertEqual(d, 0)
        self.assertEqual(self.reactions['ORE'].distance, 0)
        self.assertEqual(self.reactions['A'].distance, None)
        self.assertEqual(self.reactions['B'].distance, None)
        self.assertEqual(self.reactions['C'].distance, None)
        self.assertEqual(self.reactions['D'].distance, None)
        self.assertEqual(self.reactions['E'].distance, None)
        self.assertEqual(self.reactions['FUEL'].distance, None)


    def test1(self):
        d = distance('A', self.reactions)
        self.assertEqual(d, 1)
        self.assertEqual(self.reactions['ORE'].distance, 0)
        self.assertEqual(self.reactions['A'].distance, 1)
        self.assertEqual(self.reactions['B'].distance, None)
        self.assertEqual(self.reactions['C'].distance, None)
        self.assertEqual(self.reactions['D'].distance, None)
        self.assertEqual(self.reactions['E'].distance, None)
        self.assertEqual(self.reactions['FUEL'].distance, None)


    def test2(self):
        d = distance('FUEL', self.reactions)
        self.assertEqual(d, 5)
        self.assertEqual(self.reactions['ORE'].distance, 0)
        self.assertEqual(self.reactions['A'].distance, 1)
        self.assertEqual(self.reactions['B'].distance, 1)
        self.assertEqual(self.reactions['C'].distance, 2)
        self.assertEqual(self.reactions['D'].distance, 3)
        self.assertEqual(self.reactions['E'].distance, 4)
        self.assertEqual(self.reactions['FUEL'].distance, 5)
