import networkx as nx

from utils import printGrid
from itertools import combinations
from collections import defaultdict
from collections import Counter



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

    return grid, len(iterable[0]), len(iterable)



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



def isOuter(node, W, H):
    x, y = node
    return (x <= 2 or x >= W-2) and (y <= 2 or y >= H-2)


def isInner(node, W, H):
    x, y = node
    return (2 < x < W-3) and (2 < y < H-3)



def _collapseLabels(G0):
    """
    """
    # Fold the double letter node names
    nodes_to_delete = []
    for node in ( node for node, name in G0.nodes(data='name') if name != '.' ):
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
    nodes_to_delete = []
    #import pudb; pudb.set_trace()
    for node in ( node for node, name in G0.nodes(data='name') if name != '.' ):
        neighbours = G0[node]
        if len(neighbours) == 1:
            name = G0.nodes[node]['name']
            for neighbour in neighbours:
                G0.nodes[neighbour]['name'] = name
            nodes_to_delete.append(node)

    for node in nodes_to_delete:
        G0.remove_node(node)
    del(nodes_to_delete)

    return G0



def _findPortalLinks(G0):
    # Figure out the portals' locations
    portals = defaultdict(lambda: [])
    for node, name in ( (node, name) for node, name in G0.nodes(data='name') if name != '.' ):
        portals[name].append(node)

    return portals



def _connectWrapPortal(G0):
    for name, links in _findPortalLinks(G0).items():
        if len(links) == 1:
            G0 = nx.relabel_nodes(G0, {tuple(links)[0]: name}, copy=False)
        elif len(links) == 2:
            G0.add_edge(*tuple(links), name=name)
        elif name == '.':
            pass
        else:
            assert False, f'name: {name} links: {links}'

    return G0



def _connectWrapPortalMultilevel(G0, W, H):
    c = Counter(a for n, a in G0.nodes(data='name'))

    # Figure out the portals' locations
    portals   = _findPortalLinks(G0)
    num_level = len(portals) + 1

    # Create the multilevel Maze
    G = nx.Graph()
    for l in range(num_level):
        for node, name in G0.nodes(data='name'):
            G.add_node((*node, l), name=name)

        for (u, v, name) in G0.edges.data('name', default='.'):
            G.add_edge((*u, l), (*v, l), name=name)

    print(*portals.items(), sep='\n')
    # Connect the portal from multiple levels.
    for portal_name, coords, in portals.items():
        if len(coords) == 1:
            # This is either the entrance AA or the exit ZZ.
            coord = tuple(coords)[0] + (0,)
            G = nx.relabel_nodes(G, {coord: portal_name}, copy=False)
            for l in range(1, num_level-1):
                coord = tuple(coords)[0] + (l,)
                G = nx.relabel_nodes(G, {coord: (portal_name, l)}, copy=False)
        elif len(coords) == 2:
            for l in range(num_level-1):
                inner, outer = coords
                if isInner(outer, W, H):
                    inner, outer = outer, inner
                inner = (*inner, l)
                outer = (*outer, l+1)
                G.add_edge(inner, outer, name=portal_name)
                G.add_edge(outer, inner, name=portal_name)
        else:
            assert False, f'{portal_name}, {coords}'

    return G



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
    grid, W, H = _buildGrid(iterable)
    G0   = _fullPath(grid)
    G0   = _collapseLabels(G0)
    G0   = _connectWrapPortal(G0)
    #G    = _simplifyGraph(G0)

    return G0



def partI(data, start='AA', end='ZZ'):
    grid, W, H = _buildGrid(data)
    G   = _fullPath(grid)
    G   = _collapseLabels(G)
    G   = _connectWrapPortal(G)

    return nx.shortest_path_length(G, start, end)



def partII(data, start='AA', end='ZZ'):
    grid, W, H = _buildGrid(data)
    G   = _fullPath(grid)
    G   = _collapseLabels(G)
    G   = _connectWrapPortalMultilevel(G, W, H)
    #print(*G.nodes, sep='\n')
    #print(*((u,v,name) for u,v,name in G.edges.data('name', default=None) if name is not None), sep='\n')
    #print(*((u,v,name) for u,v,name in G.edges.data('name', default=None) if name is None), sep='\n')

    return nx.shortest_path_length(G, start, end)
