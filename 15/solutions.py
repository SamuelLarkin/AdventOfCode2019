#!/usr/bin/env  python3

import networkx as nx

from collections import defaultdict
from enum import IntEnum
from interpreter import Interpreter
from itertools import chain
from parser import parse


class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4



class Status(IntEnum):
    WALL = 0
    MOVED = 1
    OXYGEN = 2
    EMPTY = 3
    PATH = 4



moves = {
        Direction.NORTH: (0, 1),
        Direction.SOUTH: (0, -1),
        Direction.WEST: (-1, 0),
        Direction.EAST: (1, 0),
        }


opposite_move = {
        Direction.NORTH: Direction.SOUTH,
        Direction.SOUTH: Direction.NORTH,
        Direction.WEST: Direction.EAST,
        Direction.EAST: Direction.WEST,
        }



def display(grid):
    pixels = ( '#', ' ', '0', '*', '.' )
    minx, maxx = min(x for x,y in grid), max(x for x,y in grid)
    miny, maxy = min(y for x,y in grid), max(y for x,y in grid)
    print((minx, miny), (maxx, maxy))
    #print(grid)
    print(len(grid))
    for y in range(maxy - miny + 1, 0, -1):
        for x in range(maxx - minx + 1):
            if (x,y) == (21,21):
                print('S', sep='', end='')
            else:
                print(pixels[grid.get((x,y), Status.EMPTY)], sep='', end='')
        print('')



def buildGrid(pgm):
    """
    Map out the oxygen locations on the fog-of-warred grid.
    """
    edges = defaultdict(set)
    oxygen_locations = []

    def stepper(grid, position=(21,21), distance=0):
        for direction in Direction:
            move = moves[direction.value]
            new_postion = (position[0]+move[0], position[1]+move[1])
            edges[position].add(new_postion)
            if new_postion in grid:
                continue
            interpreter.giveInput(direction.value)
            status = Status(next(step))
            if status == Status.WALL:
                grid[new_postion] = Status.WALL
            elif status == Status.MOVED:
                grid[new_postion] = Status.MOVED
                stepper(grid, new_postion, distance+1)
                interpreter.giveInput(opposite_move[direction.value])
                status = Status(next(step))
                #assert status == Status.MOVED
            elif status == Status.OXYGEN:
                grid[new_postion] = Status.OXYGEN
                oxygen_locations.append((distance, new_postion))
            else:
                raise Exception(f'Invalid status {status}')

    interpreter = Interpreter(pgm)
    step = iter(interpreter)
    grid = {}
    stepper(grid)
    print(oxygen_locations)
    print([ p for p, s in grid.items() if s == Status.OXYGEN ])
    display(grid)
    return grid, edges, oxygen_locations



def partI(pgm):
    grid, edges, oxygen_locations = buildGrid(pgm)
    graph = nx.Graph()
    for v1, e in edges.items():
        for v2 in e:
            if grid[v2] != Status.WALL:
                graph.add_edge(v1, v2)
    path = nx.shortest_path(graph, (21,21), (33, 9))
    print(path)
    print(len(path))
    print(nx.shortest_path_length(graph, (21,21), (33, 9)))
    print(nx.shortest_path_length(graph, (21,21), (25, 17)))
    # Update the grid with our path to the oxygen panel
    grid.update({ p: Status.PATH for p in path })
    display(grid)



def partII(pgm):
    grid, edges, oxygen_locations = buildGrid(pgm)
    graph = nx.Graph()
    for v1, e in edges.items():
        for v2 in e:
            if grid[v2] != Status.WALL:
                graph.add_edge(v1, v2)
    oxygen = (33,9)
    print(nx.eccentricity(G, v=oxygen) + 1)  # part 2





if __name__ == '__main__':
    for status in Status:
        print(status, status.name, status.value)

    with open('input', 'r') as f:
        pgm = parse(f.readline())

    if True:
        # Answer: 208 too low
        # oxygen: (12, 12)
        partI(pgm)
