#!/usr/bin/env  python3

from parser import parse
from moons import step



if __name__ == '__main__':
    with open('input', 'r') as fin:
        planets = parse(fin.readlines())

    step(planets)
