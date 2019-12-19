#!/usr/bin/env  python3

import numpy as np

from interpreter import Interpreter
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





if __name__ == '__main__':
    pgm = loadPgm()
    partI(pgm)
