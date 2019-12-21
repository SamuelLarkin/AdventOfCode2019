#!/usr/bin/env  python3

import networkx as nx

from parser import parse



def partI(data):
    g = parse(data)

    start = 'AA'
    end = 'ZZ'

    answer = nx.shortest_path_length(g, start, end)
    print('PartI:', answer)
    assert answer, 696





if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readlines()

    if True:
        partI(data)
