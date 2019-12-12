import numpy as np


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
