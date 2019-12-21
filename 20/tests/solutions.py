#!/usr/bin/env  python3

import unittest
import networkx as nx

from .data import data1
from .data import data2
from .data import data3
from parser import partII
from utils import printEdges



class TestPartII(unittest.TestCase):
    def test3(self):
        d = partII(data3)
        self.assertEqual(d, 396)
