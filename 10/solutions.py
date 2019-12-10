#!/usr/bin/env  python3

from parser import parse
from radar import radar
from radar import laser





if __name__ == '__main__':
    with open('input', 'r') as f:
        asteroids = parse(f.readlines())

    answer = len(radar(asteroids)[1])
    # Answer: 319
    print('PartI:', answer)
    assert answer == 319

    center = radar(asteroids)[0]
    print(center)
    sequence = laser(center, asteroids)
    print(*sequence, sep='\n')
