import random

from Graph.Graph import UndirectedGraph


def build_peterson_graph():
    gu = UndirectedGraph()
    gu.add_edge(0, 1)
    gu.add_edge(1, 2)
    gu.add_edge(2, 3)
    gu.add_edge(3, 4)
    gu.add_edge(4, 0)
    gu.add_edge(0, 5)
    gu.add_edge(1, 6)
    gu.add_edge(2, 7)
    gu.add_edge(3, 8)
    gu.add_edge(4, 9)
    gu.add_edge(5, 7)
    gu.add_edge(5, 8)
    gu.add_edge(6, 8)
    gu.add_edge(6, 9)
    gu.add_edge(7, 9)
    return gu


def longest_path(g: UndirectedGraph) -> list:
    start_node = random.choice(list(g.get_nodes(0)))

    # Perform DFS to find the path
    visited = set()
    max_length_path = []

    def dfs(node, path):
        nonlocal max_length_path
        visited.add(node)
        path.append(node)

        for neighbor in g.get_adjacency_list(node):
            if neighbor not in visited:
                dfs(neighbor, path)

        if len(path) > len(max_length_path):
            max_length_path = list(path)

        path.pop()

    dfs(start_node, [])

    return max_length_path


if __name__ == '__main__':
    graph = build_peterson_graph()
    max_long_path = list(longest_path(graph))
    print(max_long_path, end=" ")
    print("the max length in this path is", len(max_long_path))
