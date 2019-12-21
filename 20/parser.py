import networkx as nx

from utils import printGrid
from itertools import combinations
from collections import defaultdict



def _buildGrid(iterable):
    """
    """
    #import pudb; pudb.set_trace()
    data = [ list(line.strip('\n')) for line in iterable ]

    grid = {}
    for y, line in enumerate(data):
        for x, name in enumerate(line):
            if name == ' ' or name == '#':
                continue
            assert 'A' <= name <= 'Z' or name == '.', f'name: {name} {x} {y}'
            grid[(x, y)] = name
    del(x)
    del(y)

    if False:
        printGrid(grid, data)

    return grid



def _fullPath(grid):
    """
    """
    G0 = nx.Graph()
    for position, name in grid.items():
        G0.add_node(position, name=name)
    assert len(G0.nodes) > 0

    for position, name in grid.items():
        for move in ((0,1), (0,-1), (1,0), (-1,0)):
            neighbour = (position[0] + move[0], position[1] + move[1]) 
            if neighbour in grid:
                G0.add_edge(position, neighbour)
    assert len(G0.edges) > 0
    del(grid)

    return G0



def computeName(info):
    return ''.join(map(lambda x: x[1], sorted(info)))



def _collapseLabels(G0):
    """
    """
    # Fold the double letter node names
    nodes_to_delete = []
    for node in G0.nodes():
        if G0.nodes[node]['name'] == '.':
            continue

        neighbours = G0[node]
        if len(neighbours) == 1:
            for neighbour in neighbours:
                # Names are in lexical order
                name = computeName( ((node, G0.nodes[node]['name']), (neighbour, G0.nodes[neighbour]['name'])) )
                G0.nodes[neighbour]['name'] = name
            nodes_to_delete.append(node)

    for node in nodes_to_delete:
        G0.remove_node(node)
    del(nodes_to_delete)

    # Label the door ways
    labels = defaultdict(lambda: set())
    nodes_to_delete = []
    #import pudb; pudb.set_trace()
    for node in G0.nodes():
        neighbours = G0[node]
        if len(neighbours) == 1:
            name = G0.nodes[node]['name']
            for neighbour in neighbours:
                labels[name].add(neighbour)
            nodes_to_delete.append(node)

    for node in nodes_to_delete:
        G0.remove_node(node)
    del(nodes_to_delete)

    for name, links in labels.items():
        if len(links) == 1:
            G0 = nx.relabel_nodes(G0, {tuple(links)[0]: name}, copy=False)
        elif len(links) == 2:
            G0.add_edge(*tuple(links), name=name)
        elif name == '.':
            pass
        else:
            assert False, f'name: {name} links: {links}'

    return G0



def _simplifyGraph(G0):
    """
    """
    ####################################
    # Start simplifying the graph.
    G = nx.Graph()
    position_of_labels = []
    for node, name in G0.nodes(data='name'):
        if name != '.':
            G.add_node(name)
            position_of_labels.append(node)
    assert len(G.nodes) > 0
    if False:
        print(*G.nodes, sep='\n')

    if False:
        #import pudb; pudb.set_trace()
        for node1, node2 in combinations(G.nodes(), 2):
            try:
                p1, p2 = tuple(map(lambda n: G.nodes[n]['position'], (node1, node2)))
                path = nx.shortest_path(G0, p1, p2)
                if len(set(path[1:-1]) & set(g.nodes)) == 0:
                    # We want direct links without intermediate links
                    G.add_edge(node1, node2, weight=len(path)-1)
            except:
                pass
    else:
        #import pudb; pudb.set_trace()
        for p1, p2 in combinations(position_of_labels, 2):
            try:
                node1 = G0.nodes[p1]['name']
                node2 = G0.nodes[p2]['name']
                path = nx.shortest_path(G0, p1, p2)
                G.add_edge(node1, node2, weight=len(path)-2)
            except:
                pass
    assert len(G.edges) > 0
    if False:
        print(*G.edges, sep='\n')

    return G



def parse(iterable):
    """
    """
    grid = _buildGrid(iterable)
    G0   = _fullPath(grid)
    G0   = _collapseLabels(G0)
    #G    = _simplifyGraph(G0)

    return G0
