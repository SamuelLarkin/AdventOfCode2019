from collections import namedtuple

Position = namedtuple('Position', ('x', 'y'))


def parse(iterable):
    asteroids = []
    for y, line in enumerate(iterable):
        line = line.strip()
        for x, asteroid in enumerate(line):
            if asteroid == '#':
                asteroids.append(Position(x, y))

    return tuple(asteroids)
