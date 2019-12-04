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

    def __repr__(self):
        return f'({self.p1}, {self.p2})'

    def __str__(self):
        return f'({self.p1}, {self.p2})'

    def __or__(self, other):
        # Vertical line
        if self.p1.x == self.p2.x:
            if other.p1.x == other.p2.x:
                return None
            else:
                if other.p1.x <= self.p1.x <= other.p2.x and self.p1.y <= other.p1.y <= self.p2.y:
                    return self.p1.x, other.p1.y
                else:
                    return None
        # Horizontal line
        else:
            if other.p1.y == other.p2.y:
                return None
            else:
                if other.p1.y <= self.p1.y <= other.p2.y and self.p1.x <= other.p1.x <= self.p1.x:
                    return other.p1.x, self.p1.y
                else:
                    return None




if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = list(map(lambda l: parse(l), f.readlines()))

    test = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
            U62,R66,U55,R34,D71,R55,D58,R83'''
    lines = list(map(lambda l: parse(l), test.splitlines()))

    print(lines)
    p1 = Point(0, 0)
    droites = []
    for x, y in lines[0]:
        p2 = Point(p1.x + x, p1.y + y)
        droites.append(Droite(p1, p2))
        p1 = p2
        
    print(droites, len(droites))

    minimum = 10000000
    p1 = Point(0, 0)
    for x, y in lines[1]:
        p2 = Point(p1.x + x, p1.y + y)
        d = Droite(p1, p2)
        p1 = p2
        print(d)

        for a in droites:
            i = d | a
            if i != None:
                distance = sum(map(abs, i))
                print(d, a)
                print(i, distance)
                minimum = min(minimum, distance)

    print(minimum)
