#!/usr/bin/env  python3

import unittest

from parser import Position
from parser import parse
from radar import laser
from radar import lineOfSight
from radar import lineOfSightRotated
from radar import lineOfSights
from radar import radar
from radar import LaserBase


class TestLineOfSight(unittest.TestCase):
    def test1(self):
        self.assertEqual(lineOfSight(Position(2,4), Position(5,1)), -0.7853981633974483)


    def test2(self):
        self.assertEqual(lineOfSight(Position(2,4), Position(2,1)), -1.5707963267948966)


    '''
    PartII wants clockwise angles and starting for up aka 0,1.
    '''
    def test3_0(self):
        center = Position(8, 3)
        self.assertEqual(lineOfSightRotated(center, Position(8,1)), LaserBase(phi=-3.141592653589793, r=2.0, x=8, y=1))
    def test3_90(self):
        center = Position(8, 3)
        self.assertEqual(lineOfSightRotated(center, Position(10,3)), LaserBase(phi=-1.5707963267948966, r=2.0, x=10, y=3))
    def test3_180(self):
        center = Position(8, 3)
        self.assertEqual(lineOfSightRotated(center, Position(8,5)), LaserBase(phi=0., r=2.0, x=8, y=5))
    def test3_270(self):
        center = Position(8, 3)
        self.assertEqual(lineOfSightRotated(center, Position(6,3)), LaserBase(phi=1.5707963267948966, r=2.0, x=6, y=3))



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



class TestLaser(unittest.TestCase):
    def test1(self):
        def extract(l):
            return (l.x, l.y)

        data = '''.#....#####...#..
        ##...##.#####..##
        ##...#...#.#####.
        ..#.....X...###..
        ..#.#.....#....##'''.splitlines()
        center = Position(8, 3)
        sequence = laser(center, parse(data))
        #print(*sequence, sep='\n')
        self.assertEqual(extract(sequence[0]), (8,1))
        self.assertEqual(extract(sequence[1]), (9,0))
        self.assertEqual(extract(sequence[2]), (9,1))
        self.assertEqual(extract(sequence[3]), (10,0))
        self.assertEqual(extract(sequence[8]), (15,1))

        self.assertEqual(extract(sequence[9]), (12,2))
        self.assertEqual(extract(sequence[17]), (4,4))
