#!/usr/bin/env  python3

import unittest
import networkx as nx

from .data import data1
from .data import data2
from parser import parse
from solutions import second_shortest_path
from utils import printEdges



class TestSecondShortestPath(unittest.TestCase):
    def test1(self):
        g = parse(data1)
        printEdges(g)
        self.assertEqual(len(g.nodes), 5)
        self.assertEqual(len(g.edges), 8)
        d = second_shortest_path(g, 'AA', 'ZZ')
        self.assertEqual(d, 28)


    def test2(self):
        #import pudb; pudb.set_trace()
        g = parse(data2)
        printEdges(g)
        self.assertEqual(len(g.nodes()), 12)
        d = second_shortest_path(g, 'AA', 'ZZ')
        self.assertEqual(d, 58)
