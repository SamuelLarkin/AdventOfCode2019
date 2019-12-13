import numpy as np

from itertools import count

def influence(planets):
    """
    Calculate the pairwise influence of planets on each other.
    (num_coord, num_planet, num_planet)
    """
    num_planet = planets.shape[0]
    num_coord = planets.shape[1]
    influence = np.zeros((num_coord, num_planet, num_planet), dtype=np.int32)
    test = np.expand_dims(planets.T, 1) - np.expand_dims(planets.T, 2)
    influence[test < 0] = -1
    influence[test > 0] = 1

    return influence



def velocity(influence):
    """
    Given the planets' influences on each other, calculate the velocity change.
    (num_coord, num_planet, num_planet) => (num_coord, num_planet)
    """
    return influence.sum(axis=2)



def step(planets_pos, planets_vel):
    """
    planets_pos => (num_planet, num_coord)
    planets_vel => (num_planet, num_coord)
    """
    planet_influences = influence(planets_pos)
    planets_vel += velocity(planet_influences).T


    return planets_pos + planets_vel, planets_vel



def energy(planets_pos, planets_vel):
    """
    Calculates the total amount of energy.
    planets_pos => (num_planet, num_coord)
    planets_vel => (num_planet, num_coord)
    """
    answer = np.sum(np.absolute(planets_pos).sum(1) * np.absolute(planets_vel).sum(1))
    return answer



def tuplize(planets):
    return tuple(planets.tolist())



def tuplize_all(*planets):
    #return tuple(tuplize(planets_pos), tuplize(planets_vel))
    return tuple(tuplize(i) for i in planets)



def repeated(planets_pos, planets_vel):
    """
    planets_pos => (num_planet, num_coord)
    planets_vel => (num_planet, num_coord)
    """
    periods = [ [] for _ in range(3) ]
    seen = [ set(tuplize_all(pp, pv)) for pp, pv in zip(planets_pos.T, planets_vel.T) ]

    for it in count(0):
        planets_pos, planets_vel = step(planets_pos, planets_vel)
        for s, period, pp, pv in zip(seen, periods, planets_pos.T, planets_vel.T):
            info = tuplize_all(pp, pv)
            if info in s:
                period.append(it)
            s.add(info)
        if all( len(a) > 0 for a in periods ):
            break

    periods = [ p[0] for p in periods ]
    return np.lcm.reduce(periods)
