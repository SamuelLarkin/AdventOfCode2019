#!/usr/bin/env  python3

import unittest

from parser import parse
from parser import Reaction



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
            'A': Reaction(multiplier=10, reactants={'ORE': 10}),
            'B': Reaction(multiplier=1, reactants={'ORE': 1}),
            'C': Reaction(multiplier=1, reactants={'A': 7, 'B': 1}),
            'D': Reaction(multiplier=1, reactants={'A': 7, 'C': 1}),
            'E': Reaction(multiplier=1, reactants={'A': 7, 'D': 1}),
            'FUEL': Reaction(multiplier=1, reactants={'A': 7, 'E': 1}),
            })
