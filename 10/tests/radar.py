#!/usr/bin/env  python3

import unittest

from parser import Position
from parser import parse
from radar import lineOfSight
from radar import lineOfSights
from radar import radar


class TestLineOfSight(unittest.TestCase):
    def test1(self):
        self.assertEqual(lineOfSight(Position(2,4), Position(5,1)), -0.7853981633974483)


    def test2(self):
        self.assertEqual(lineOfSight(Position(2,4), Position(2,1)), -1.5707963267948966)



inf = float('inf')

class TestRadar(unittest.TestCase):
    def test1a(self):
        """
        .7..7
        .....
        67775
        ....7
        ...87
        """
        data = '''.#..#
        .....
        #####
        ....#
        ...##'''.splitlines()
        los = lineOfSights(parse(data))
        self.assertEqual(len(los[Position(x=1, y=0)]), 7)
        self.assertEqual(len(los[Position(x=4, y=0)]), 7)
        self.assertEqual(len(los[Position(x=0, y=2)]), 6)
        self.assertEqual(len(los[Position(x=1, y=2)]), 7)  # <=
        self.assertEqual(len(los[Position(x=2, y=2)]), 7)
        self.assertEqual(len(los[Position(x=3, y=2)]), 7)
        self.assertEqual(len(los[Position(x=4, y=2)]), 5)
        self.assertEqual(len(los[Position(x=4, y=3)]), 7)
        self.assertEqual(len(los[Position(x=3, y=4)]), 8)
        self.assertEqual(len(los[Position(x=4, y=4)]), 7)


    def test1b(self):
        data = '''.#..#
        .....
        #####
        ....#
        ...##'''.splitlines()
        los = lineOfSights(parse(data))
        self.assertEqual(los, {
            Position(x=1, y=0): {0.0, 1.5707963267948966, 2.0344439357957027, 0.7853981633974483, 1.1071487177940904, 0.5880026035475675, 0.9272952180016122},
            Position(x=4, y=0): {1.5707963267948966, 2.5535900500422257, 2.677945044588987, 3.141592653589793, 2.356194490192345, 2.0344439357957027, 1.8157749899217608},
            Position(x=0, y=2): {-0.4636476090008061, 0.0, 0.5880026035475675, 0.24497866312686414, 0.4636476090008061, -1.1071487177940904},
            Position(x=1, y=2): {-0.5880026035475675, 0.0, 0.3217505543966422, 3.141592653589793, 0.7853981633974483, 0.5880026035475675, -1.5707963267948966},
            Position(x=2, y=2): {-0.7853981633974483, 0.0, 0.4636476090008061, 3.141592653589793, 1.1071487177940904, 0.7853981633974483, -2.0344439357957027},
            Position(x=3, y=2): {0.0, 0.7853981633974483, 1.5707963267948966, 3.141592653589793, 1.1071487177940904, -2.356194490192345, -1.1071487177940904},
            Position(x=4, y=2): {1.5707963267948966, 2.0344439357957027, 3.141592653589793, -2.5535900500422257, -1.5707963267948966},
            Position(x=4, y=3): {1.5707963267948966, 2.356194490192345, -2.819842099193151, -2.896613990462929, -2.356194490192345, -2.677945044588987, -1.5707963267948966},
            Position(x=3, y=4): {-0.7853981633974483, 0.0, -1.3258176636680326, -2.356194490192345, -2.0344439357957027, -1.1071487177940904, -2.5535900500422257, -1.5707963267948966},
            Position(x=4, y=4): {3.141592653589793, -2.5535900500422257, -2.356194490192345, -2.214297435588181, -2.0344439357957027, -2.677945044588987, -1.5707963267948966},
            })


    def test2(self):
        data = '''.#..#
        .....
        #####
        ....#
        ...##'''.splitlines()
        max_los = radar(parse(data))
        self.assertEqual(max_los[0], Position(3,4))
        self.assertEqual(len(max_los[1]), 8)


    def test3(self):
        data = '''......#.#.
        #..#.#....
        ..#######.
        .#.#.###..
        .#..#.....
        ..#....#.#
        #..#....#.
        .##.#..###
        ##...#..#.
        .#....####'''.splitlines()
        max_los = radar(parse(data))
        self.assertEqual(max_los[0], Position(5,8))
        self.assertEqual(len(max_los[1]), 33)


    def test4(self):
        data = '''#.#...#.#.
        .###....#.
        .#....#...
        ##.#.#.#.#
        ....#.#.#.
        .##..###.#
        ..#...##..
        ..##....##
        ......#...
        .####.###.'''.splitlines()
        max_los = radar(parse(data))
        self.assertEqual(max_los[0], Position(1,2))
        self.assertEqual(len(max_los[1]), 35)


    def test5(self):
        data = '''.#..#..###
        ####.###.#
        ....###.#.
        ..###.##.#
        ##.##.#.#.
        ....###..#
        ..#.#..#.#
        #..#.#.###
        .##...##.#
        .....#.#..'''.splitlines()
        max_los = radar(parse(data))
        self.assertEqual(max_los[0], Position(6,3))
        self.assertEqual(len(max_los[1]), 41)


    def test6(self):
        data = '''.#..##.###...#######
        ##.############..##.
        .#.######.########.#
        .###.#######.####.#.
        #####.##.#.##.###.##
        ..#####..#.#########
        ####################
        #.####....###.#.#.##
        ##.#################
        #####.##.###..####..
        ..######..##.#######
        ####.##.####...##..#
        .#####..#.######.###
        ##...#.##########...
        #.##########.#######
        .####.#.###.###.#.##
        ....##.##.###..#####
        .#.#.###########.###
        #.#.#.#####.####.###
        ###.##.####.##.#..##'''.splitlines()
        max_los = radar(parse(data))
        self.assertEqual(max_los[0], Position(11,13))
        self.assertEqual(len(max_los[1]), 210)


