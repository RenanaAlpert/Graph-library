from Graph.Graph import DirectedGraph
from Graph.TraversalAlgorithms import bfs
from Graph.ShortestPaths import find_path


def create_flow_graph(g: DirectedGraph) -> DirectedGraph:
    flow_graph = DirectedGraph()
    for edge in g.get_edges():
        flow_graph.add_edge(edge[0], edge[1], {'c': edge[2], 'f': 0})
    return flow_graph


def create_residual_network(flow_graph: DirectedGraph) -> DirectedGraph:
    residual_network = DirectedGraph()
    for edge_from in flow_graph.get_nodes(0):
        for edge_to, weight in flow_graph.get_adjacency_list(edge_from).items():
            flow = weight['f']
            capacity = weight['c']
            if capacity - flow > 0:
                residual_network.add_edge(edge_from, edge_to, capacity - flow)
            if flow > 0:
                residual_network.add_edge(edge_to, edge_from, flow)
    # for edge_from, edge_to, weight in flow_graph.get_edges():
    #     flow = weight['f']
    #     capacity = weight['c']
    #     if capacity - flow > 0:
    #         residual_network.add_edge(edge_from, edge_to, capacity - flow)
    #     if flow > 0:
    #         residual_network.add_edge(edge_to, edge_from, flow)
    return residual_network


def find_augmenting_path(residual_network: DirectedGraph, src, sink) -> tuple[int, list | None]:
    bfs(residual_network, src)
    path = find_path(residual_network, src, sink)
    if not path:
        return 0, None
    min_flow = min(residual_network.get_adjacency_list(path[i])[path[i+1]] for i in range(1, len(path) - 1))
    return min_flow, path
    # min_flow = residual_network.get_adjacency_list(path[0])[path[1]]
    # for i in range(1, len(path) - 1):
    #     flow = residual_network.get_adjacency_list(path[i])[path[i+1]]
    #     if flow < min_flow:
    #         min_flow = flow


def ford_fulkerson(g: DirectedGraph, src, sink) -> tuple[int, DirectedGraph]:
    flow_graph = create_flow_graph(g)
    flow = 0
    while True:
        residual_network = create_residual_network(flow_graph)
        min_flow, path = find_augmenting_path(residual_network, src, sink)
        if path is None:
            break
        for i in range(len(path) - 1):
            from_edge = path[i]
            to_edge = path[i+1]
            if to_edge in flow_graph.get_adjacency_list(from_edge):
                flow_graph.get_adjacency_list(from_edge)[to_edge]['f'] += min_flow
            else:
                flow_graph.get_adjacency_list(to_edge)[from_edge]['f'] -= min_flow
        flow += min_flow

    return flow, flow_graph
