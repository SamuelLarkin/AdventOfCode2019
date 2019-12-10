#!/usr/bin/env  python3

from parser import parse
from radar import radar






if __name__ == '__main__':
    with open('input', 'r') as f:
        asteroids = parse(f.readlines())

    answer = len(radar(asteroids)[1])
    print('PartI:', answer)
