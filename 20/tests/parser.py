#!/usr/bin/env  python3

import unittest
import networkx as nx

from parser import parse
from parser import _buildGrid
from parser import _fullPath
from parser import _collapseLabels
from parser import _simplifyGraph
from .data import data1
from .data import data2
from collections import Counter



class TestBuildGrid(unittest.TestCase):
    def test1(self):
        grid = _buildGrid(data1)
        self.assertEqual(len(grid), 63)



class TestFullPath(unittest.TestCase):
    def test1(self):
        G = _fullPath(_buildGrid(data1))
        self.assertEqual(len(G.edges), 60)



class TestCollapseLabels(unittest.TestCase):
    def test1(self):
        G = _collapseLabels(_fullPath(_buildGrid(data1)))
        self.assertEqual(len(G.edges), 52)
        self.assertEqual(Counter(a for n, a in G.nodes('name')), Counter({'.': 47, 'BC': 2, 'DE': 2, 'FG': 2, 'AA': 1, 'ZZ': 1}))



class TestParser(unittest.TestCase):
    def test1(self):
        g = parse(data1)
        self.assertEqual(len(g.nodes), 5)
        self.assertEqual(len(g.edges), 8)
        self.assertEqual(nx.shortest_path_length(g, 'AA', 'BC'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'AA', 'FG'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'AA', 'ZZ'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'BC', 'DE'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'BC', 'FG'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'BC', 'ZZ'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'DE', 'FG'), 1)
        self.assertEqual(nx.shortest_path_length(g, 'FG', 'ZZ'), 1)
        #self.assertEqual(nx.shortest_path_length('AA', 'BC'), 5)
        #self.assertEqual(nx.shortest_path_length('BC', 'DE'), 7)
        #self.assertEqual(nx.shortest_path_length('DE', 'FG'), 5)
        #self.assertEqual(nx.shortest_path_length('DE', 'FG'), 7)


    def test2(self):
        g = parse(data2)
        self.assertEqual(len(g.nodes()), 22)
