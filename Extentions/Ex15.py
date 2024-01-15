from Graph.Graph import DirectedGraph
from Graph.TraversalAlgorithms import strongly_connected_components, dfs as t_dfs
from Graph import Node


def build_graph():
    g = DirectedGraph()
    g.add_edge('s', 'v')
    g.add_edge('v', 'w')
    g.add_edge('w', 's')
    g.add_edge('g', 's')
    g.add_edge('g', 'w')
    g.add_edge('g', 'l')
    g.add_edge('l', 'x')
    g.add_edge('l', 'y')
    g.add_edge('x', 'z')
    g.add_edge('z', 'x')
    g.add_edge('y', 'g')
    g.add_edge('r', 'y')
    g.add_edge('r', 'u')
    g.add_edge('u', 'y')
    return g


def is_bipartite(g: DirectedGraph):
    def dfs(g: DirectedGraph, src: Node) -> bool:
        src.info['color'] = 'g'
        for neighbor in g.get_adjacency_list(src.get_value()):
            n = g.get_node(neighbor)
            if n.info['color'] == 'w':
                n.info['side'] = 1 - src.info['side']
                if not dfs(g, n):
                    return False
            elif n.info['side'] == src.info['side']:
                return False
        src.info['color'] = 'b'
        return True

    t_dfs(g)
    g.sort(lambda node: node[1].info['f'], True)

    nodes = g.get_nodes(1)
    for n in nodes:
        n.info = {'color': 'w'}
    for n in nodes:
        if n.info['color'] == 'w':
            for nei in g.get_adjacency_list(n.get_value()):
                if g.get_node(nei).info['color'] != 'w':
                    n.info['side'] = 1 - g.get_node(nei).info['side']
            if 'side' not in n.info.keys():
                n.info['side'] = 0
            if not dfs(g, n):
                return False
    return True


def is_bipartite_dfs(g):
    # Function to perform DFS and check if the graph is bipartite
    def dfs(node, color):
        colors[node] = color
        for neighbor in g.get_adjacency_list(node):
            if neighbor not in colors:
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True

    # Dictionary to store the color of each vertex
    colors = {}

    # Iterate through all vertices in case the graph is disconnected
    for vertex in g.get_nodes(0):
        if vertex not in colors:
            if not dfs(vertex, 0):
                return False

    return True


if __name__ == '__main__':
    g = build_graph()
    print(strongly_connected_components(g))
    print(is_bipartite(g))
    g.remove_edge('w', 's')
    g.remove_edge('y', 'g')
    g.remove_edge('u', 'y')
    print(is_bipartite(g))
    g.remove_node('g')
    print(is_bipartite(g))
