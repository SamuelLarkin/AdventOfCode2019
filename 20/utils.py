def printEdges(g):
    #print(*map(lambda nn: tuple(map(lambda n: g.nodes[n]['name'], nn)), g.edges), sep='\n')
    print(*g.edges, sep='\n')



def printGrid(grid, data):
    for y, line in enumerate(data):
        for x, name in enumerate(line):
            print(grid.get((x,y), ' '), sep='', end='')
        print('')
