#!/usr/bin/env  python3

import networkx as nx
import parser



def partI(data):
    answer = parser.partI(data)
    print('PartI:', answer)
    assert answer, 696



def partII(data):
    answer = parser.partII(data)
    # 3654 too low
    print('PartI:', answer)
    assert answer, 696





if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readlines()

    if True:
        partI(data)

    if True:
        partII(data)
