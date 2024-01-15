from Graph.Graph import *
# from TraversalAlgorithms import topological_sort
import numpy as np
# import pandas as pd
import heapq as hq


# def dag_shortest_path(g: DirectedGraph) -> pd.DataFrame:
#     nodes = list(g.get_nodes(1))
#     dist = pd.DataFrame(np.full((len(nodes), len(nodes)), np.inf), columns=g.get_nodes(0), index=g.get_nodes(0))
#     topologic = topological_sort(g)
#     for node in topologic:
#         for neighbor, weight in g.get_adjacency_list(node).items():
#             if dist.loc
#
#     return dist


def dijkstra(g: DirectedGraph, src):
    """
    Implement Dijkstra algorithm
    :param g: a directed non-weighted graph
    :param src: the source node
    :return: None
    """
    nodes = list(g.get_nodes(1))
    heap = []
    for n in nodes:
        n.info = {'pi': None, 'key': np.inf}
        if n.get_value() == src:
            n.info['key'] = 0
            heap.append(n)
    visited = {k: False for k in g.get_nodes(0)}
    hq.heapify(heap)
    while heap:
        mini = hq.heappop(heap)
        val = mini.get_value()
        visited[val] = True
        for label, weight in g.get_adjacency_list(val).items():
            n = g.get_node(label)
            if visited[label] is False:
                dist = mini.info['key'] + weight
                if dist < n.info['key']:
                    n.info['pi'] = val
                    n.info['key'] = dist
                    hq.heappush(heap, n)


def find_path(g, src, dest):
    path = []
    child = dest
    while child is not None and child != src:
        path.insert(0, child)
        child = g.get_node(child).info['pi']
    if child == src:
        path.insert(0, child)
    else:
        # print(f"There is no path between {src} to {dest}")
        path = []
    return path


def bellman_ford(g: DirectedGraph, src) -> bool:
    """
    Implement bellman ford algorithm
    :param g: a directed weighted(with negative weighted) graph
    :param src: the source node
    :return: True if there is solution else False
    """
    nodes = list(g.get_nodes(1))
    for n in nodes:
        n.info = {'pi': None, 'key': np.inf}
        if n.get_value() == src:
            n.info['key'] = 0
    for i in range(len(nodes) - 1):
        for n in nodes:
            val = n.get_value()
            for label, weight in g.get_adjacency_list(val).items():
                nei = g.get_node(label)
                dist = n.info['key'] + weight
                if dist < nei.info['key']:
                    nei.info['pi'] = val
                    nei.info['key'] = dist
    for n in nodes:
        val = n.get_value()
        for label, weight in g.get_adjacency_list(val).items():
            nei = g.get_node(label)
            if n.info['key'] + weight < nei.info['key']:
                return False
    return True


def difference_constraints(inequality_matrix: np.array, right_side_vector: np.array) -> DirectedGraph:
    """
    implement difference constraints algorithms
    :param inequality_matrix: matrix of np.Array
    :param right_side_vector: 1D np.Array
    :return: directed graph
    """
    graph = DirectedGraph()
    for i in range(inequality_matrix.shape[1]):
        graph.add_edge('start', i + 1, 0)

    for line in range(inequality_matrix.shape[0]):
        from_node = np.where(inequality_matrix[line] == -1)[0]
        to_node = np.where(inequality_matrix[line] == 1)[0]
        weight = right_side_vector[line]
        graph.add_edge(from_node[0] + 1, to_node[0] + 1, weight)

    return graph


def floyd_warshall(g: DirectedGraph) -> np.array:
    """
    Implement of floyd warshall algorithm
    :param g: a directed weighted graph
    :return: matrix with all the distance between all pair of nodes
    """
    nodes = list(g.get_nodes(1))
    dist = np.full((len(nodes), len(nodes)), np.inf)
    for i in range(dist.shape[0]):
        dist[i][i] = 0

    for val in g.get_nodes(0):
        for label, weight in g.get_adjacency_list(val).items():
            dist[g.get_node(val).get_id()][g.get_node(label).get_id()] = weight

    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
