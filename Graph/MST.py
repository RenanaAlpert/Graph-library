from Graph.Graph import *
import numpy as np
import heapq as hq


class UnionFind:

    def __init__(self, group: set = None):
        if group is None:
            group = {}
        self.parent = {n: n for n in group}
        self.capacity = len(group)

    def make(self, *args):
        for item in args:
            self.parent[item] = item
            self.capacity += 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_y != root_x:
            self.parent[root_y] = root_x
            self.capacity -= 1

    def num_sets(self):
        return self.capacity


def kruskal(g: DirectedGraph) -> DirectedGraph:
    """
    implement kruskal's algorithm
    :param g: the graph to compute on it
    :return: the MST in the given graph
    """
    nodes = g.get_nodes(0)
    uf = UnionFind(nodes)
    edges = g.get_edges()
    edges = sorted(edges, key=lambda edge: edge[2], reverse=False)
    mst = UndirectedGraph() if isinstance(g, UndirectedGraph) else DirectedGraph()
    for edge in edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            mst.add_edge(*edge)
            uf.union(edge[0], edge[1])
            if uf.num_sets() == 1:
                return mst
    return mst


def prim(g: DirectedGraph, src) -> DirectedGraph:
    """
    Implement prim algorithm
    :param g: a directed graph
    :param src: the source node
    :return: the MST in the given graph
    """
    nodes = list(g.get_nodes(1))
    heap = []
    for n in nodes:
        n.info = {'pi': None, 'key': np.inf}
        if n.get_value() == src:
            n.info['key'] = 0
            heap.append(n)
    mst = UndirectedGraph() if isinstance(g, UndirectedGraph) else DirectedGraph()
    visited = {k: False for k in g.get_nodes(0)}
    hq.heapify(heap)
    while heap:
        mini = hq.heappop(heap)
        val = mini.get_value()
        if visited[val]:
            continue
        if val != src:
            mst.add_edge(mini.info['pi'], val, mini.info['key'])
        visited[val] = True
        for label, weight in g.get_adjacency_list(val).items():
            n = g.get_node(label)
            if not visited[label] and weight < n.info['key']:
                n.info['pi'] = val
                n.info['key'] = weight
                hq.heappush(heap, n)
    return mst
