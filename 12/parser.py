import numpy as np


def parse(iterable):
    planets = []
    for line in iterable:
        line = line.strip()[1:-1].split(',')
        planet = [ int(p.strip().split('=')[1]) for p in line ]
        planets.append(planet)

    return np.array(planets, dtype=np.int32)
