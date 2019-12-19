#!/usr/bin/env  python3

import unittest

from tunnel import scan1
from tunnel import buildGraph
from tunnel import loadTunnel
from tunnel import simplifyGraph
from tunnel import exploreBFS



data1 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''.splitlines()

data2 = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''.splitlines()

class TestScan1(unittest.TestCase):
    def test1(self):
        data = '''#########
        #b.A.@.a#
        #########'''.splitlines()
        grid, keys, doors, entrance = scan1(data)

        self.assertEqual(grid, {(7, 1), (6, 1), (3, 1), (2, 1), (5, 1), (4, 1), (1, 1)})
        self.assertEqual(keys, {(1, 1), (7,1)})
        self.assertEqual(doors, {(3,1)})
        self.assertEqual(entrance, (5,1))


    def test2(self):
        grid, keys, doors, entrance = scan1(data1)

        self.assertEqual(grid, {(7, 3), (1, 3), (12, 1), (9, 1), (20, 3), (2, 1), (15, 1), (17, 3), (5, 1), (10, 3), (18, 1), (22, 2), (3, 3), (13, 3), (8, 1), (21, 1), (16, 3), (6, 3), (14, 1), (11, 1), (19, 3), (4, 1), (1, 1), (12, 3), (22, 3), (7, 1), (15, 3), (9, 3), (20, 1), (17, 1), (2, 3), (10, 1), (5, 3), (13, 1), (8, 3), (18, 3), (6, 1), (3, 1), (11, 3), (21, 3), (16, 1), (4, 3), (14, 3), (22, 1), (19, 1)})
        self.assertEqual(keys, {(1, 3), (7, 1), (21, 1), (17, 1), (11, 1), (1, 1)})
        self.assertEqual(doors, {(13, 1), (9, 1), (3, 1), (5, 1), (19, 1)})
        self.assertEqual(entrance, (15,1))



class TestBuildGraph(unittest.TestCase):
    def test1(self):
        grid, keys, doors, entrance = scan1(data1)
        G = buildGraph(grid)



class TestSimplifyGraph(unittest.TestCase):
    def test2(self):
        grid, keys, doors, entrance = scan1(data2)
        G = buildGraph(grid)
        G = simplifyGraph(G, grid, keys, doors, entrance)
        print(*sorted(G.nodes), sep='\n')
        print(*sorted(G.edges), sep='\n')
        print(G[entrance])
        print(*list(G.adjacency()), sep='\n')
        self.assertEqual(len(G.nodes), 13)
        self.assertEqual(len(G.edges), 12)



class TestLoadTunnel(unittest.TestCase):
    def test1(self):
        #import pudb; pudb.set_trace()
        loadTunnel(data1)



class TestExploreBFS(unittest.TestCase):
    def test1(self):
        grid, keys, doors, entrance = scan1(data2)
        G = buildGraph(grid)
        G = simplifyGraph(G, grid, keys, doors, entrance)
        d = exploreBFS(G, grid, keys, doors, entrance)
        print(d)
