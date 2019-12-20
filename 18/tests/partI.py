#!/usr/bin/env  python3

import unittest

from tunnel import partI



class TestPartI(unittest.TestCase):
    def test1(self):
        """
        key sequence: a, c, f, i, d, g, b, e, h
        """
        data = '''#########
        #b.A.@.a#
        #########'''.splitlines()
        expected = 8
        self.assertEqual(partI(data), expected)


    def test2(self):
        """
        key sequence: b, a, c, d, f, e, g
        """
        data = '''########################
        #f.D.E.e.C.b.A.@.a.B.c.#
        ######################.#
        #d.....................#
        ########################'''.splitlines()
        expected = 86
        self.assertEqual(partI(data), expected)


    def test3(self):
        """
        key sequence: b, a, c, d, f, e, g
        """
        data = '''########################
        #...............b.C.D.f#
        #.######################
        #.....@.a.B.c.d.A.e.F.g#
        ########################'''.splitlines()
        expected = 132
        self.assertEqual(partI(data), expected)


    def test4(self):
        """
        key sequence: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m
        """
        data = '''#################
        #i.G..c...e..H.p#
        ########.########
        #j.A..b...f..D.o#
        ########@########
        #k.E..a...g..B.n#
        ########.########
        #l.F..d...h..C.m#
        #################'''.splitlines()
        expected = 136
        self.assertEqual(partI(data), expected)


    def test5(self):
        """
        key sequence: a, c, f, i, d, g, b, e, h
        """
        data = ''' ########################
        #@..............ac.GI.b#
        ###d#e#f################
        ###A#B#C################
        ###g#h#i################
        ########################'''.splitlines()
        expected = 81
        self.assertEqual(partI(data), expected)
