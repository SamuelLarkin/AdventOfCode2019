import networkx as nx
import heapq
from itertools import combinations



def scan1(data = None):
    grid = {}
    keys = set()
    doors = set()
    entrance = None
    key_names = { str(chr(x)) for x in range(ord('a'), ord('z')+1) }
    door_names = { str(chr(x)) for x in range(ord('A'), ord('Z')+1) }
    for y, line in enumerate(data):
        for x, status in enumerate(line.strip()):
            position = (x, y)
            if status == '#':
                continue
            if status == '@':
                entrance = position
            elif status in key_names:
                keys.add(position)
            elif status in door_names:
                doors.add(position)
            #else:
            #    raise Exception(f'Unknown status {status}')
            grid[position] = status

    return grid, keys, doors, entrance



def buildGraph(grid):
    G = nx.Graph()
    for position in grid:
        for move in ((1,0), (-1,0), (0,1), (0,-1)):
            new_position = (position[0]+move[0], position[1]+move[1])
            if new_position in grid:
                G.add_edge(position, new_position)

    return G



def explore(G, grid, keys, doors, current_position, pass_locations=[], num_steps=0, found_keys={}):
    """
    return [
    num_steps:int, [locations]
    ]
    """
    if len(keys) == 0 and len(doors) == 0:
        return [(num_steps, pass_locations)]

    possible_destinations = []
    for position in keys:
        path = nx.shortest_path(G, current_position, position)
        if doors & set(path):
            # There is door blocking the way.
            continue
        possible_destinations.append((len(path)-1, position, path))

    for position in doors:
        path = nx.shortest_path(G, current_position, position)
        if set(path[:-1]) & doors:
            # Other than the current door, if there is an unopened door in that path, we can't use this.
            continue
        if grid[position].lower() in found_keys:
            # If we don't have the key, it is a waste of time to visite that position.
            possible_destinations.append((len(path)-1, position, path))

    solutions = []
    for len_path, p, path in possible_destinations:
        if p in doors:
            # TODO: remove the door from the grid & doors list.
            solutions.extend(explore(G, grid, keys, { d for d in doors if d != p }, p, pass_locations+[p], num_steps+len_path, found_keys))
        elif p in keys:
            solutions.extend(explore(G, grid, { k for k in keys if k != p }, doors, p, pass_locations+[p], num_steps+len_path, {**found_keys, grid[p]: p}))
        else:
            assert False

    return solutions



def simplifyGraph(G, grid, keys, doors, entrance):
    #import pudb; pudb.set_trace()
    Gs = nx.Graph()
    obj = keys | doors | {entrance}
    for o in obj:
        Gs.add_node(grid[o], coord=o)

    for p1, p2 in combinations(obj, 2):
        path = nx.shortest_path(G, p1, p2)
        if set(path[1:-1]) & obj:
            continue
        Gs.add_edge(grid[p1], grid[p2], weight=len(path)-1)

    #Gs.nodes.data('label')
    #NodeDataView({(22, 3): 'g', (20, 3): 'F', (8, 3): 'a', (6, 3): None, (10, 3): 'B', (18, 3): 'e', (16, 3): 'A', (14, 3): 'd', (20, 1): 'D', (18, 1): 'C', (22, 1): 'f', (16, 1): 'b', (12, 3): 'c'}, data='label')
    #Gs.nodes.data('type')
    #NodeDataView({(22, 3): 'key', (20, 3): 'door', (8, 3): 'key', (6, 3): 'entrance', (10, 3): 'door', (18, 3): 'key', (16, 3): 'door', (14, 3): 'key', (20, 1): 'door', (18, 1): 'door', (22, 1): 'key', (16, 1): 'key', (12, 3): 'key'}, data='type')
    #Gs.nodes.data()
    #NodeDataView({(22, 3): {'type': 'key', 'label': 'g'}, (20, 3): {'type': 'door', 'label': 'F'}, (8, 3): {'type': 'key', 'label': 'a'}, (6, 3): {'type':'entrance', 'label': None}, (10, 3): {'type': 'door', 'label': 'B'}, (18, 3): {'type': 'key', 'label': 'e'}, (16, 3): {'type': 'door', 'label': 'A'},(14, 3): {'type': 'key', 'label': 'd'}, (20, 1): {'type': 'door', 'label': 'D'}, (18, 1): {'type': 'door', 'label': 'C'}, (22, 1): {'type': 'key','label': 'f'}, (16, 1): {'type': 'key', 'label': 'b'}, (12, 3): {'type': 'key', 'label': 'c'}})

    return Gs




def exploreBFS(G, grid, keys, doors, entrance):
    def updateGraph(g, f, t):
        # [networkx.Graph.copy](https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.Graph.copy.html)
        #g2 = nx.Graph(g)
        g2 = g.copy(as_view=False)
        weight = g2.edges[f,t]['weight']
        for neighbour in g2[f]:
            if neighbour == t:
                continue
            #g2.add_edge(t, neighbour, weight=weight+g2.edges[f, neighbour]['weight'])
            g2.add_edge(t, neighbour, weight=nx.shortest_path_length(g2, t, neighbour, 'weight'))
        g2.remove_node(f)
        return g2

    #import pudb; pudb.set_trace()
    delme = nx.get_node_attributes(G, 'type')
    works = []
    # (distance, node/position, acquired_keys, G)
    heapq.heappush(works, (0, entrance, set(), G))
    while len(works) > 0:
        distance, node, acquired_keys, GG = heapq.heappop(works)
        if len(acquired_keys) == len(keys):
            return distance

        for neighbour in GG[node]:
            if GG.nodes[neighbour]['type'] == 'door':
                if GG.nodes[neighbour]['label'].lower() not in acquired_keys:
                    continue
            work = (
                distance + GG.edges[node, neighbour]['weight'],
                neighbour, 
                acquired_keys & {GG.nodes[neighbour]['label']} if GG.nodes[neighbour]['type'] == 'key' else acquired_keys,
                updateGraph(GG, node, neighbour))
            heapq.heappush(works, work)



def isDoor(node):
    return 'A' <= node <= 'Z'



def isKey(node):
    return 'a' <= node <= 'z'


def doorKey(door):
    """
    What is the key needed for this door.
    """
    return door.lower()



def exploreBFS2(G0):
    #import pudb; pudb.set_trace()
    def updateGraph(g0, f, t):
        # [networkx.Graph.copy](https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.Graph.copy.html)
        #g2 = nx.Graph(g)
        g = g0.copy(as_view=False)
        for neighbour in g0[f]:
            if neighbour == t:
                continue
            g.add_edge(t, neighbour, weight=nx.shortest_path_length(g0, t, neighbour, 'weight'))
        g.remove_node(f)
        return g

    works = []
    seen_work = set()
    # (distance, node/position, acquired_keys, G)
    work = (0, '@', tuple(), G0)
    heapq.heappush(works, work)
    seen_work.add(work)
    while len(works) > 0:
        #print(len(works))
        #print(*works, sep='\n')
        distance, node, acquired_keys, G = heapq.heappop(works)
        if len(G.nodes) == 1:
            return distance

        for neighbour in G[node]:
            if isDoor(neighbour) and doorKey(neighbour) not in acquired_keys:
                continue
            work = (
                distance + G.edges[node, neighbour]['weight'],
                neighbour, 
                acquired_keys + (neighbour,) if isKey(neighbour) else acquired_keys,
                updateGraph(G, node, neighbour))
            if work[:-1] not in seen_work:
                heapq.heappush(works, work)
                seen_work.add(work[:-1])

    return distance



def loadTunnel(data = None):
    if data is None:
        with open('input', 'r') as f:
            data = f.readlines()

    grid, keys, doors, entrance = scan1(data)
    #print('keys:', *keys, sep='\n')
    #print('doors:', *doors, sep='\n')
    #print('grid:', *grid, sep='\n')
    G = buildGraph(grid)
    #print(*G.edges(), sep='\n')
    import pudb; pudb.set_trace()
    a = explore(G, grid, keys, doors, entrance)
    #print(*sorted(a), sep='\n')
    print(min(a))

    return min(a)[0]



def partI(data):
    grid, keys, doors, entrance = scan1(data)
    G = buildGraph(grid)
    G = simplifyGraph(G, grid, keys, doors, entrance)
    d = exploreBFS2(G)

    return d
