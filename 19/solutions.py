#!/usr/bin/env  python3

import numpy as np

from interpreter import Interpreter
from itertools import count
from parser import loadPgm



def partI(pgm):
    grid = []
    for y in range(50):
        line = []
        for x in range(50):
            interpreter = Interpreter(pgm)
            step = iter(interpreter)
            interpreter.giveInputs((x,y))
            line.append(next(step))
        grid.append(line)

    print(*grid, sep='\n')
    answer = sum(sum(line) for line in grid)
    print('PartI:', answer)
    assert answer == 201



def partII(pgm):
    def check(x, y):
        interpreter = Interpreter(pgm)
        step = iter(interpreter)
        interpreter.giveInputs((x,y))
        return next(step)

    x = 10
    y = 150
    while True:
        for x in count(x):
            if check(x, y) == 1:
                break
        print(f'x:{x}, y:{y}')
        if check(x+99, y-99) == 1:
            return x, y-99
        y += 1




if __name__ == '__main__':
    pgm = loadPgm()

    partI(pgm)

    x, y = partII(pgm)
    # BAD 6670993
    print('PartII:', x*10000+y)
