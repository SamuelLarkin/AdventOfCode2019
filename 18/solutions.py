#!/usr/bin/env  python3

from tunnel import exploreBFS2
from tunnel import scan1
from tunnel import buildGraph
from tunnel import simplifyGraph


def partI():
    with open('input', 'r') as f:
        grid, keys, doors, entrance = scan1(f)
    G = buildGraph(grid)
    G = simplifyGraph(G, grid, keys, doors, entrance)
    d = exploreBFS2(G)
    print(d)




if __name__ == '__main__':
    partI()
