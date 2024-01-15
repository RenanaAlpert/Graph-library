from Graph.Graph import DirectedGraph
from Graph.TraversalAlgorithms import topological_sort


def build_graph():
    g = DirectedGraph()
    g.add_edge('m', 'x')
    g.add_edge('m', 'q')
    g.add_edge('m', 'r')
    g.add_edge('n', 'q')
    g.add_edge('n', 'u')
    g.add_edge('q', 't')
    g.add_edge('u', 't')
    g.add_edge('r', 'u')
    g.add_edge('n', 'o')
    g.add_edge('o', 'r')
    g.add_edge('o', 's')
    g.add_edge('s', 'r')
    g.add_edge('o', 'v')
    g.add_edge('r', 'y')
    g.add_edge('y', 'v')
    g.add_edge('v', 'x')
    g.add_edge('p', 'o')
    g.add_edge('p', 's')
    g.add_edge('p', 'z')
    g.add_edge('v', 'w')
    g.add_edge('w', 'z')
    return g


if __name__ == '__main__':
    g = build_graph()
    print(topological_sort(g))
