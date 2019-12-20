#!/usr/bin/env  python3

import unittest
import networkx as nx

from parser import parse
from .data import data1
from .data import data2



class TestParser(unittest.TestCase):
    def test1(self):
        g, start, end = parse(data1)
        self.assertEqual(len(g.nodes()), 8)


    def test2(self):
        g, start, end = parse(data2)
        self.assertEqual(len(g.nodes()), 22)
