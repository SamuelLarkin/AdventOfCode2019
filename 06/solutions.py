#!/usr/bin/env python3


from collections import defaultdict


def crc(orbits):
    def helper(moons, current_orbit=0):
        if len(moons) == 0:
            return current_orbit
        return sum(map(lambda planet: helper(crc[planet], current_orbit+1), moons)) + current_orbit

    orbits = list(map(str.strip, orbits))
    orbits = list(map(lambda o: tuple(o.split(')')), orbits))
    print(orbits)

    planets = set( planet for orbit in orbits for planet in orbit )
    print(planets)
    print(len(planets))

    crc = defaultdict(lambda: set())
    for planet, moon in orbits:
        crc[planet].add(moon)

    print(crc)
    
    return helper(crc['COM'])



def crc2(orbits):
    def helper(planet, current_orbit=0):
        if planet in ('SAN', 'YOU'):
            return current_orbit
        moons = crc[planet]
        if len(moons) == 0:
            return 0
        return sum(map(lambda planet: helper(planet, current_orbit+1), moons))

    orbits = list(map(str.strip, orbits))
    orbits = list(map(lambda o: tuple(o.split(')')), orbits))
    print(orbits)

    planets = set( planet for orbit in orbits for planet in orbit )
    print(planets)
    print(len(planets))

    crc = defaultdict(lambda: set())
    for planet, moon in orbits:
        crc[planet].add(moon)

    print(crc)
    
    possible_solutions = [ (planet, helper(planet)) for planet in planets ]
    print(possible_solutions)



def crc3(orbits):
    def helper(planet, current_orbit=0):
        if planet in ('SAN', 'YOU'):
            return current_orbit
        moons = crc[planet]
        if len(moons) == 0:
            return 0
        return sum(map(lambda planet: helper(planet, current_orbit+1), moons))

    def find_parents(planet):
        answer = set()
        while planet != 'COM':
            parent = parents[planet]
            answer.add(parent)
            planet = parent
        return answer

    orbits = list(map(str.strip, orbits))
    orbits = list(map(lambda o: tuple(o.split(')')), orbits))
    print(orbits)

    crc = defaultdict(lambda: set())
    for planet, moon in orbits:
        crc[planet].add(moon)

    parents = { moon: planet for planet, moon in orbits }
    print(parents)

    possible_solutions = [ (planet, helper(planet)) for planet in find_parents('YOU') & find_parents('SAN') ]
    print(possible_solutions)

    return sorted(possible_solutions, key=lambda x: x[1])[0][1] - 2





if __name__ == '__main__':
    with open('input', 'r') as f:
        orbits = f.readlines()

    # Answer: 147223
    print(crc(orbits))

    # Answer: 340
    print(crc3(orbits))
