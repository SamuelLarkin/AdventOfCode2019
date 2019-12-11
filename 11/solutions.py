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
        print(color, direction)

    print('colors:', colors)
    print('visits:', visits)
    # Answer: 1985
    print('PartI:', len(visits))
