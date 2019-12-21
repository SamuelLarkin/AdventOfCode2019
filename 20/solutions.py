#!/usr/bin/env  python3

import networkx as nx


def second_shortest_path(graph, start, end):
    g = nx.Graph(graph)
    #if len(nx.shortest_path(g, start, end)) == 2:
    #    g.remove_edge(start, end)

    print(nx.shortest_path(g, start, end, weight='weight'))
    return nx.shortest_path_length(g, start, end, weight='weight')





if __name__ == '__main__':
    pass
