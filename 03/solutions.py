#!/usr/bin/env python3

import numpy as np

from collections import namedtuple


def parseSingleInstruction(m, d):
    """
    Parse a single instruction.
    """
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


def parseInstructions(line):
    """
    Parse a all instructions.
    """
    line = line.strip().split(',')
    line = [ parseSingleInstruction(move[0], int(move[1:])) for move in line ]
    return line


Point = namedtuple('Point', ('x', 'y'))

class Droite:
    """
    Holds two Points that define a Droite.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    @property
    def len(self):
        return ManhattonDistance(self.p1, self.p2)


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
        """
        Calculate the intersection between two Droites or return None if they don't intersect.
        """
        if self.isVertical() and other.isVertical():
            return None

        if not self.isVertical() and not other.isVertical():
            return None

        vertical, horizontal = (self, other) if self.isVertical() else (other, self)

        if horizontal.x_min <= vertical.p1.x <= horizontal.x_max:
            if vertical.y_min <= horizontal.p1.y <= vertical.y_max:
                return Point(vertical.p1.x, horizontal.p1.y)

        return None



def ManhattonDistance(p1, p2=Point(0, 0)):
    """
    Calculate the Manhattan distance between two points.
    """
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)



def minimumDistance(wire1, wire2):
    wire1_segments = []
    p1 = Point(0, 0)
    for x, y in wire1:
        p2 = Point(p1.x + x, p1.y + y)
        wire1_segments.append(Droite(p1, p2))
        p1 = p2

    print(wire1_segments, len(wire1_segments))

    minimums_distance = []  # Manhattan distances between origin and intersections
    minimums_step = []  # Total wires' length when wires cross.

    distance2 = 0  # wire 2's length
    p1 = Point(0, 0)
    for x, y in wire2:
        p2 = Point(p1.x + x, p1.y + y)
        d2 = Droite(p1, p2)
        p1 = p2
        print(d2)

        distance1 = 0  # wire 1's length
        for d1 in wire1_segments:
            # Calculate intersection point.
            intersecting_point = d2 | d1
            # Are they intersecting?
            if intersecting_point != None:
                distance = ManhattonDistance(intersecting_point)
                minimums_distance.append(distance)

                steps = distance1 \
                        + distance2 \
                        + ManhattonDistance(intersecting_point, d1.p1) \
                        + ManhattonDistance(intersecting_point, d2.p1)
                minimums_step.append(steps)

                print(d2, d1)
                print(intersecting_point, distance)
            distance1 += d1.len

        distance2 += d2.len

    minimums_distance = list(filter(lambda d: d!=0, minimums_distance))
    minimums_distance.sort()
    print(minimums_distance)

    minimums_step = list(filter(lambda d: d!=0, minimums_step))
    minimums_step.sort()
    print(minimums_step)

    return minimums_distance[0], minimums_step[0]





if __name__ == '__main__':
    test = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
              U62,R66,U55,R34,D71,R55,D58,R83'''
    wires = list(map(lambda l: parseInstructions(l), test.splitlines()))

    md, steps = minimumDistance(*wires)
    assert md == 159
    assert steps == 610


    test = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
              U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
    wires = list(map(lambda l: parseInstructions(l), test.splitlines()))

    md, steps = minimumDistance(*wires)
    assert md == 135
    assert steps == 410


    if True:
        with open('input', 'r') as f:
            wires = list(map(lambda l: parseInstructions(l), f.readlines()))

        # Answers: 1337 & 65356
        print(minimumDistance(*wires))
