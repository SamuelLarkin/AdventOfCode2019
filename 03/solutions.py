#!/usr/bin/env python3

import numpy as np

from collections import namedtuple


def subparse(m, d):
    if m == 'U':
        p2 = (0, d)
    elif m == 'D':
        p2 = (0, -d)
    elif m == 'R':
        p2 = (d, 0)
    elif m == 'L':
        p2 = (-d, 0)
    else:
        raise Exception(f'Invalid move {m}')

    return p2


def parse(line):
    line = line.strip().split(',')
    line = [ subparse(move[0], int(move[1:])) for move in line ]
    return line


class Axe:
    def __init__(self):
        self.position, self.min, self.max = 0, 0, 0

    def __iadd__(self, a):
        self.position += a
        self.max = max(self.max, self.position)
        return self

    def __isub__(self, a):
        self.position -= a
        self.min = min(self.min, self.position)
        return self

    def __str__(self):
        return f'{self.position}  [{self.min, self.max}]'


class Position:
    def __init__(self):
        self.x = Axe()
        self.y = Axe()

    def __str__(self):
        return f'x: {self.x}  y: {self.y}'



Point = namedtuple('Point', ('x', 'y'))

class Droite:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    @property
    def x_min(self):
        return min(self.p1.x, self.p2.x)


    @property
    def x_max(self):
        return max(self.p1.x, self.p2.x)


    @property
    def y_min(self):
        return min(self.p1.y, self.p2.y)


    @property
    def y_max(self):
        return max(self.p1.y, self.p2.y)


    def __repr__(self):
        return f'({self.p1}, {self.p2})'


    def __str__(self):
        return f'({self.p1}, {self.p2})'


    def isVertical(self):
        return self.p1.x == self.p2.x


    def __or__(self, other):
        if self.isVertical() and other.isVertical():
            return None

        if not self.isVertical() and not other.isVertical():
            return None

        vertical, horizontal = (self, other) if self.isVertical() else (other, self)

        if horizontal.x_min <= vertical.p1.x <= horizontal.x_max:
            if vertical.y_min <= horizontal.p1.y <= vertical.y_max:
                return Point(vertical.p1.x, horizontal.p1.y)

        return None



def ManhattonDistance(point):
    return sum(map(abs, point))



def minimumDistance(wire1, wire2):
    p1 = Point(0, 0)
    droites = []
    for x, y in wire1:
        p2 = Point(p1.x + x, p1.y + y)
        droites.append(Droite(p1, p2))
        p1 = p2

    print(droites, len(droites))

    minimums = []
    p1 = Point(0, 0)
    for x, y in wire2:
        p2 = Point(p1.x + x, p1.y + y)
        d = Droite(p1, p2)
        p1 = p2
        print(d)

        for a in droites:
            intersecting_point = d | a
            if intersecting_point != None:
                distance = ManhattonDistance(intersecting_point)
                print(d, a)
                print(intersecting_point, distance)
                minimums.append(distance)

    print(minimums)
    minimums.sort()
    minimums = list(filter(lambda d: d!=0, minimums))

    return minimums[0]





if __name__ == '__main__':
    test = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
              U62,R66,U55,R34,D71,R55,D58,R83'''
    wires = list(map(lambda l: parse(l), test.splitlines()))

    print(minimumDistance(*wires))

    test = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
              U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
    wires = list(map(lambda l: parse(l), test.splitlines()))

    print(minimumDistance(*wires))


    with open('input', 'r') as f:
        wires = list(map(lambda l: parse(l), f.readlines()))

    print(minimumDistance(*wires))
