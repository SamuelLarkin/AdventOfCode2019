#!/usr/bin/env  python3

import numpy as np

from collections import defaultdict
from interpreter import Interpreter
from parser import parse

from enum import IntEnum

class TileType(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def solve_partI(pgm):
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

    minx, maxx = min( x for x, y in grid.keys() ),  max( x for x, y in grid.keys() )
    miny, maxy = min( y for x, y in grid.keys() ),  max( y for x, y in grid.keys() )

    # TODO: display map
    maze = np.zeros((maxx-minx+1, maxy-miny+1), dtype=np.int8)
    for (x, y), tile_id in grid.items():
        maze[x, y] = tile_id
    print(maze)

    # Answer: 213
    print('Part I:', len(tiles[2]))



def solve_partII(pgm):
    pgm[0] = 2
    interpreter = Interpreter(pgm)
    grid = {}
    
    def init_grid():
        for _ in range(24 * 36):
            x = interpreter()
            if x is None:
                break
            y = interpreter()
            tile_id = interpreter()
            if x == -1 and y == 0:
                score = tile_id
            else:
                grid[x,y] = tile_id


    def update_grid(inp):
        tile_id = None
        score = 0
        while tile_id != TileType.BALL.value:
            x = interpreter(inp)
            if x is None:
                break
            y = interpreter(inp)
            tile_id = interpreter(inp)
            if x == -1 and y == 0:
                score = tile_id
            else:
                grid[x, y] = tile_id

        return score

    
    def joystick(grid):
        """
        """
        ball   = [k for k, v in grid.items() if v == TileType.BALL.value][0][0]
        paddle = [k for k, v in grid.items() if v == TileType.PADDLE.value][0][0]
        if paddle < ball:
            return 1
        elif paddle > ball:
            return -1
        return 0


    score = 0
    init_grid()
    while True:
        num_block = len(list(filter(lambda tid: tid == TileType.BLOCK.value, grid.values())))
        if num_block == 0:
            break
        score = update_grid(joystick(grid))
        print(f'{score} > {num_block}')

    # Answer: 11441
    print('Part II:', score)





if __name__ == '__main__':
    with open('input', 'r') as f:
        pgm = parse(f.readline())

    if False:
        solve_partI(pgm)

    solve_partII(pgm)
