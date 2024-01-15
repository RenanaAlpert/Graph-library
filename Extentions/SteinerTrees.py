from Graph.Graph import UndirectedGraph
from Graph.MST import kruskal
from Graph.ShortestPaths import dijkstra, find_path


def build_graph():
    g = UndirectedGraph()
    g.add_edge('a', 'b', 1)
    g.add_edge('b', 'f', 5)
    g.add_edge('a', 'd', 4)
    g.add_edge('d', 'b', 4)
    g.add_edge('d', 'e', 2)
    g.add_edge('c', 'b', 6)
    g.add_edge('c', 'e', 3)
    g.add_edge('f', 'e', 2)
    return g


def steiner(g: UndirectedGraph, terminal: set) -> UndirectedGraph:
    steiner_graph = UndirectedGraph()
    if terminal is None or terminal == {}:
        return steiner_graph

    mst = kruskal(g)
    src = terminal.pop()
    dijkstra(mst, src)
    for item in terminal:
        path = find_path(mst, src, item)
        for n in range(len(path) - 1):
            steiner_graph.add_edge(path[n], path[n + 1], mst.get_adjacency_list(path[n])[path[n+1]])
    return steiner_graph


if __name__ == '__main__':
    g = build_graph()
    print(steiner(g, {'a', 'b', 'c', 'd', 'e', 'f'}).get_edges())
    print(steiner(g, {'a', 'b', 'e'}).get_edges())
