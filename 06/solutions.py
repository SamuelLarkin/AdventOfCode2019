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

    planets = set( planet for orbit in orbits for planet in orbit)
    print(planets)
    print(len(planets))

    crc = defaultdict(lambda: set())
    for planet, moon in orbits:
        crc[planet].add(moon)

    print(crc)
    
    return helper(crc['COM'])





if __name__ == '__main__':
    test = '''COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L'''
    print(crc(test.splitlines()))

    if True:
        with open('input', 'r') as f:
            orbits = f.readlines()
        print(crc(orbits))
