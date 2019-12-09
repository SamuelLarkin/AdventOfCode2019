#!/usr/bin/env python3


def calculateFull(mass):
    """
    Calculate the required fuel for a given mass.
    """
    return mass // 3 -2



def otherFuel(mass):
    """
    Recursively require the fuel require for a mass and its fuel.
    """
    submass = calculateFull(mass)
    if submass <= 0:
        return 0
    return submass + otherFuel(submass)




if __name__ == '__main__':
    with open('input', 'r') as f:
        fuel = sum(map(lambda x: calculateFull(int(x.strip())), f.readlines()))

    print('part1', fuel)

    with open('input', 'r') as f:
        fuel = sum(map(lambda x: otherFuel(int(x.strip())), f.readlines()))

    print('part2', fuel)

