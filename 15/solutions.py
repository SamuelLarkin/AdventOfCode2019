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



origine = (21, 21)



def display(grid):
    pixels = ( '#', ' ', '0', '*', '.' )
    minx, maxx = min(x for x,y in grid), max(x for x,y in grid)
    miny, maxy = min(y for x,y in grid), max(y for x,y in grid)
    print((minx, miny), (maxx, maxy))
    #print(grid)
    print(len(grid))
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) == origine:
                print('S', sep='', end='')
            else:
                print(pixels[grid.get((x,y), Status.EMPTY)], sep='', end='')
        print('')



def buildGrid(pgm):
    """
    Map out the oxygen locations on the fog-of-warred grid.
    """
    print('Building/Discovering the grid...')
    edges = defaultdict(set)
    oxygen_locations = []

    def stepper(grid, position=origine, distance=0):
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
                oxygen_locations.append(new_postion)
                interpreter.giveInput(opposite_move[direction.value])
                status = Status(next(step))
            else:
                raise Exception(f'Invalid status {status}')

    interpreter = Interpreter(pgm)
    step = iter(interpreter)
    grid = {}
    stepper(grid)
    assert len(oxygen_locations) == 1, f'oxygen_locations: {oxygen_locations}'
    oxygen_location = oxygen_locations[0]
    print('Oxygen location:', oxygen_location)
    print([ p for p, s in grid.items() if s == Status.OXYGEN ])
    display(grid)

    return grid, edges, oxygen_location



def partI(grid, edges, oxygen_location):
    """
    Shortest path to the oxygen panel
    """
    print('Finding shortest path to oxygen panel...')
    graph = nx.Graph()
    for v1, e in edges.items():
        for v2 in e:
            if grid[v2] != Status.WALL:
                graph.add_edge(v1, v2)
    path = nx.shortest_path(graph, origine, oxygen_location)
    print(path)
    print(len(path))
    answer = nx.shortest_path_length(graph, origine, oxygen_location)
    print('Part I:', answer)
    assert answer == 208
    # Update the grid with our path to the oxygen panel
    grid.update({ p: Status.PATH for p in path })
    display(grid)



def partII(grid, edges, oxygen_location):
    """
    How long to fill the room
    """
    print('Computing time to fill room with oxygen...')
    graph = nx.Graph()
    for v1, e in edges.items():
        for v2 in e:
            if grid[v2] != Status.WALL:
                graph.add_edge(v1, v2)
    # Answer: 306
    answer = nx.eccentricity(graph, v=oxygen_location)
    print('Part II:', answer)
    assert answer == 306





if __name__ == '__main__':
    for status in Status:
        print(status, status.name, status.value)

    with open('input', 'r') as f:
        pgm = parse(f.readline())
    grid, edges, oxygen_location = buildGrid(pgm)

    if True:
        # Answer: 208 too low
        # oxygen: (12, 12)
        partI(grid, edges, oxygen_location)

    if True:
        partII(grid, edges, oxygen_location)
