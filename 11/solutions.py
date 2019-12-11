#!/usr/bin/env  python3

from collections import defaultdict
from parser import parse
from interpreter import Interpreter
from robot import Robot





if __name__ == '__main__':
    with open('input', 'r') as f:
        pgm = parse(f.readline())

    colors = defaultdict(lambda: 0)
    visits = defaultdict(lambda: 0)

    interpreter = Interpreter(pgm)
    robot = Robot()

    for _ in range(10020):
        color = interpreter(colors[robot.position])
        if color is None:
            break
        colors[robot.position] = color
        direction = interpreter()
        assert direction is not None
        robot.step(direction)
        visits[robot.position] += 1
        #print(color, direction)

    #print('colors:', colors)
    #print('visits:', visits)
    # Answer: 1985
    print('PartI:', len(visits))


    ####################################
    # PART II
    colors = defaultdict(lambda: 0)
    visits = defaultdict(lambda: 0)

    interpreter = Interpreter(pgm)
    robot = Robot()

    colors[robot.position] = 1
    for _ in range(10020):
        color = interpreter(colors[robot.position])
        if color is None:
            break
        colors[robot.position] = color
        direction = interpreter()
        assert direction is not None
        robot.step(direction)
        visits[robot.position] += 1
        #print(color, direction)

    print('colors:', colors)
    print('visits:', visits)
    a = (min(map(lambda x: x[0], colors.keys())), min(map(lambda x: x[1], colors.keys())))
    b = (max(map(lambda x: x[0], colors.keys())), max(map(lambda x: x[1], colors.keys())))

    print(a,b)
    image = [ [0 for x in range(45) ] for y in range(6) ]
    for coord, color in colors.items():
        image[-coord[1]][coord[0]] = color

    for line in image:
        for p in line:
            print('#' if p == 1 else ' ', sep='', end='')
        print('')

    print('PartI:', 'BLCZCJLZ')
