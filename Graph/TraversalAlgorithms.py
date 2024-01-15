from Graph.Graph import *
import numpy as np
from queue import Queue


def initialize_bfs(nodes: list[Node], src_node) -> Node:
    """
    initialize args in order to BFS algorithm
    :param nodes: list of all the node in the graph to do BFS on it
    :param src_node: the label of the source node
    :return: the source node
    """
    src = None
    for n in nodes:
        if n.get_value() == src_node:
            src = n
            n.info = {'color': 'g', 'd': 0}
        else:
            n.info = {'color': 'w', 'd': np.inf}
        n.info['pi'] = None
    return src


def bfs(g: DirectedGraph, src_node):
    """
    Implement of BFS algorithm
    :param g: the graph to traversal on it
    :param src_node: the source node
    :return: None
    """
    nodes = g.get_nodes(1)
    src = initialize_bfs(nodes, src_node)
    q = Queue()
    q.put(src)
    while not q.empty():
        u = q.get()
        for neighbor in g.get_adjacency_list(u.get_value()):
            n = g.get_node(neighbor)
            if n.info['color'] == 'w':
                n.info['color'] = 'g'
                n.info['d'] = u.info['d'] + 1
                n.info['pi'] = u.get_value()
                q.put(n)
        u.info['color'] = 'b'


def predecessor(g: DirectedGraph, src) -> DirectedGraph:
    """
    BFS predecessor graph
    :param g: which graph to compute
    :param src: the node to start with
    :return: the BFS predecessor graph of the given graph
    """
    bfs(g, src)
    bfs_predecessor_graph = UndirectedGraph() if isinstance(g, UndirectedGraph) else DirectedGraph()

    bfs_predecessor_graph.add_node(src)
    for node in g.get_nodes(1):
        if node.info['pi'] is not None:
            bfs_predecessor_graph.add_edge(node.info['pi'], node.get_value())

    return bfs_predecessor_graph


def dfs_visit(g: DirectedGraph, src: Node, time: int) -> int:
    """
    the recursion of the DFS algorithm
    :param g: the graph to traversal on it
    :param src: the source node. where to start the recursion
    :param time: which time we are on it
    :return: the new time for the next recursions
    """
    time += 1
    src.info['d'] = time
    src.info['color'] = 'g'
    for neighbor in g.get_adjacency_list(src.get_value()):
        n = g.get_node(neighbor)
        if n.info['color'] == 'w':
            n.info['pi'] = src.get_value()
            time = dfs_visit(g, n, time)
    src.info['color'] = 'b'
    time = time + 1
    src.info['f'] = time
    return time


def dfs(g: DirectedGraph):
    """
    Implement of DFS algorithm
    :param g: the graph to traversal on it.
    :return: None
    """
    nodes = g.get_nodes(1)
    for n in nodes:
        n.info = {'color': 'w', 'pi': None, 'd': np.inf, 'f': None}
    time = 0
    for n in nodes:
        if n.info['color'] == 'w':
            time = dfs_visit(g, n, time)


def strongly_connected_components(g: DirectedGraph) -> list[list]:
    """
    compute all the strongly connected components of the given graph
    :param g: a directed graph
    :return: list of all components
    """
    dfs(g)
    g.sort(lambda node: node[1].info['f'], True)
    g_reverse = g.graph_reverse()
    dfs(g_reverse)
    scc = []
    scc_list = []
    for n in reversed(g_reverse.get_nodes(1)):
        scc.insert(0, n.get_value())
        if n.info['pi'] is None:
            scc_list.insert(0, scc)
            scc = []
    return scc_list


def topological_sort(g: DirectedGraph) -> list[Node]:
    """
    implement topological sort
    :param g: acyclic directed graph. The graph have to be DAG
    :return:
    """
    dfs(g)
    g.sort(lambda node: node[1].info['f'], True)
    return g.get_nodes(0)
