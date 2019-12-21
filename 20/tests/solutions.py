#!/usr/bin/env  python3

import unittest
import networkx as nx

from .data import data1
from .data import data2
from .data import data3
from parser import partI
from parser import partII
from utils import printEdges



class TestPartI(unittest.TestCase):
    def test1(self):
        d = partI(data1)
        self.assertEqual(d, 23)


    def test2(self):
        d = partI(data2)
        self.assertEqual(d, 58)



class TestPartII(unittest.TestCase):
    def test1(self):
        d = partII(data1)
        self.assertEqual(d, 26)


    def test2(self):
        with self.assertRaises(nx.NetworkXNoPath):
            d = partII(data2)


    def test3(self):
        d = partII(data3)
        self.assertEqual(d, 396)
