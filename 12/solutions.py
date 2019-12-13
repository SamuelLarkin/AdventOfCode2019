#!/usr/bin/env  python3

from parser import parse
from moons import step
from moons import energy
from moons import repeated

import numpy as np



if __name__ == '__main__':
    with open('input', 'r') as fin:
        planets_pos = parse(fin.readlines())
        planets_vel = np.zeros_like(planets_pos)

    for _ in range(1000):
        planets_pos, planets_vel = step(planets_pos, planets_vel)
    answer = energy(planets_pos, planets_vel)
    # Answer: 7722
    print('Part I:', answer)


    with open('input', 'r') as fin:
        planets_pos = parse(fin.readlines())
        planets_vel = np.zeros_like(planets_pos)

    answer = repeated(planets_pos, planets_vel)
    # Answer: 292653556339368
    print('Part II:', answer)
