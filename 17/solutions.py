#!/usr/bin/env  python3

import networkx

from interpreter import Interpreter
from parser import loadPgm



class Position:
    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __hash__(self):
        return (self.x, self.y).__hash__()



def partI():
    pgm = loadPgm()
    interpreter = Interpreter(pgm)
    step = iter(interpreter)

    position = Position()
    grid = {}
    for s in step:
        s = str(chr(s))
        print(s, sep='', end='')
        if s == '\n':
            position = position + Position(0, 1)
            position.x = 0
            continue
        elif s == '#':
            grid[position] = set()
        elif s in ('^', 'v', '<', '>'):
            grid[position] = set()
            start = position
        position = position + Position(1, 0)

    for position in grid.keys():
        for move in (Position(1,0), Position(-1,0), Position(0,1), Position(0,-1)):
            if position + move in grid:
                grid[position].add(position + move)

    print(grid)
    answer = 0
    for node, edges in grid.items():
        if len(edges) == 4:
            answer += node.x * node.y


    print('PartI:', answer)
    assert answer == 8928



def partII():
    pass





if __name__ == '__main__':
    partI()
    partII()
