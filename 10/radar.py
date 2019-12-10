from parser import Position
import cmath


def lineOfSight(center, asteroid):
    x = float(asteroid.x - center.x)
    y = float(asteroid.y - center.y)
    c = complex(x, y)

    return cmath.polar(c)[1]



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
