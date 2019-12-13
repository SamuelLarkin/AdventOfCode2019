#!/usr/bin/env  python3

from collections import defaultdict

from interpreter import Interpreter
from parser import parse


if __name__ == '__main__':
    with open('input', 'r') as f:
        pgm = parse(f.readline())

    interpreter = Interpreter(pgm)

    tiles = defaultdict(lambda: [])
    grid = {}

    while True:
        x = interpreter()
        if x is None:
            break
        y = interpreter()
        tile_id = interpreter()
        grid[(x,y)] = tile_id
        tiles[tile_id].append((x,y))

    # Answer: 213
    print('Part I:', len(tiles[2]))

    # TODO: display map
    


    interpreter = Interpreter(pgm)
    score = None
    while True:
        x = interpreter()
        if x is None:
            break
        y = interpreter()
        tile_id = interpreter()
        if x == -1 and y == 0:
            score = tile_id
