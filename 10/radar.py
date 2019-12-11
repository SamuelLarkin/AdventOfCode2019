import cmath
from collections import namedtuple
from itertools import cycle
from itertools import groupby
from itertools import islice
from parser import Position


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))



def lineOfSight(center, asteroid):
    x = float(asteroid.x - center.x)
    y = float(asteroid.y - center.y)
    c = complex(x, y)
    return cmath.polar(c)[1]



LaserBase = namedtuple('LaserBase', ('phi', 'r', 'x', 'y'))
class Laser(LaserBase):
    def __init__(self, phi, r, x, y):
        LaserBase.__init__(self, phi, r, x, y)

    def __new__(cls, phi, r, x, y):
        self = super(Laser, cls).__new__(cls, phi, r, x, y)



def lineOfSightRotated(center, asteroid):
    x = float(asteroid.x - center.x)
    y = float(asteroid.y - center.y)
    c = complex(y, -x)
    coordinates = cmath.polar(c)
    #if coordinates[1] == -3.141592653589793:
    #    coordinates = (coordinates[0], -coordinates[1])

    #return LaserBase((coordinates[1] - cmath.pi/2.) % cmath.pi, coordinates[0], asteroid.x, asteroid.y)
    return LaserBase(coordinates[1], coordinates[0], asteroid.x, asteroid.y)



def lineOfSights(asteroids):
    los = {}
    for center in asteroids:
        los[center] = set( lineOfSight(center, asteroid) for asteroid in filter(lambda a: a != center, asteroids) )
        assert len(los[center]) < len(asteroids), 'Too many lines of sight'
    assert len(los) == len(asteroids)

    #print(*los.items(), sep='\n')

    return los



def radar(asteroids):
    los = lineOfSights(asteroids)

    return max( los.items(), key=lambda a: len(a[1]) )



def laser(center, asteroids):
    sequence = [ lineOfSightRotated(center, asteroid) for asteroid in filter(lambda a: a!=center, asteroids) ]

    sequence = sorted(sequence, key=lambda x: (x.phi, x.r))

    sequence = list(roundrobin( *[list(g) for k, g in groupby(sequence, key=lambda x: x.phi)]))

    return sequence
