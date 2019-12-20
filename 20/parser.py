import networkx as nx

from utils import printGrid
from itertools import combinations



def parse(iterable):
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

    # Fold the double letter node names
    nodes_to_delete = []
    for node in G0.nodes():
        if G0.nodes[node]['name'] == '.':
            continue

        neighbours = G0[node]
        if len(neighbours) == 1:
            for neighbour in neighbours:
                # Names are in lexical order
                name = ''.join(sorted((G0.nodes[node]['name'], G0.nodes[neighbour]['name'])))
                G0.nodes[neighbour]['name'] = name
                nodes_to_delete.append(node)

    for node in nodes_to_delete:
        G0.remove_node(node)
    del(nodes_to_delete)


    ####################################
    # Start simplifying the graph.
    G = nx.Graph()
    for node, name in G0.nodes(data='name'):
        if name != '.':
            G.add_node(name)
    assert len(G.nodes) > 0

    import pudb; pudb.set_trace()
    for node1, node2 in combinations(G.nodes(), 2):
        try:
            p1, p2 = tuple(map(lambda n: G.nodes[n]['position'], (node1, node2)))
            path = nx.shortest_path(G0, p1, p2)
            if len(set(path[1:-1]) & set(g.nodes)) == 0:
                # We want direct links without intermediate links
                G.add_edge(node1, node2, weight=len(path)-1)
        except:
            pass
    assert len(G.edges) > 0

    start = [ n for n, attributes in G.nodes(data=True) if attributes['name'] == 'AA' ]
    assert len(start) == 1
    start = start[0]
    end = [ n for n, attributes in G.nodes(data=True) if attributes['name'] == 'ZZ' ]
    assert len(end) == 1, f'{end}'
    end = end[0]

    return G, start, end
