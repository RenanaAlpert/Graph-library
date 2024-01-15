from Graph.Node import Node


# import numpy as np


class DirectedGraph:
    """
    This class represents a directed weighted graph.
    """

    def __init__(self):
        """ Constructor """
        self.__nodes = {}
        self.__adjacency_list_in = {}
        self.__adjacency_list_out = {}
        self.__counter_nodes = 0

    def add_node(self, label):
        """
        create new node in the graph
        :param label: the value of the new node
        :return: None
        """
        new_node = Node(label, self.__counter_nodes)
        self.__counter_nodes += 1
        self.__nodes[label] = new_node
        # if self.__matrix_neighbors is None:
        #     self.__matrix_neighbors = np.array([[0]])
        # else:
        #     new_neighbors = np.zeros(new_node.get_id())
        #     np.vstack(self.__matrix_neighbors, new_neighbors)
        #     new_neighbors = np.zeros(new_node.get_id() + 1)
        #     np.hstack(self.__matrix_neighbors, new_neighbors)

    def add_edge(self, label_from, label_to, weight=1):
        """
        create new edge in the graph
        :param label_from: node the edge out from
        :param label_to: node the edge come into
        :param weight: the weight of the edge
        :return:
        """
        if label_from not in self.__nodes:
            self.add_node(label_from)
        if label_to not in self.__nodes:
            self.add_node(label_to)

        if label_from not in self.__adjacency_list_out:
            self.__adjacency_list_out[label_from] = {}
        if label_to not in self.__adjacency_list_in:
            self.__adjacency_list_in[label_to] = {}

        self.__adjacency_list_out[label_from][label_to] = weight
        self.__adjacency_list_in[label_to][label_from] = weight
        # edge_from = self.__nodes[label_from].get_id()
        # edge_to = self.__nodes[label_to].get_id()
        # self.__matrix_neighbors[edge_from, edge_to] = weight

    def get_adjacency_list(self, label) -> dict:
        """
        find all the neighbors of the given node
        :param label: value of the node
        :return: dict of the neighbors and the weights
        """
        if label in self.__adjacency_list_out:
            return self.__adjacency_list_out[label]
        return {}

        # src_node = self.__nodes[label].get_id()
        # if self.__matrix_neighbors is None or label not in self.__nodes:
        #     raise ValueError(f"there is no node with label {label}")
        # neighbors = []
        # for label, node in self.__nodes.items():
        #     id_node = node.get_id()
        #     if self.__matrix_neighbors[src_node, id_node] > 0:
        #         neighbors.append(node)
        # return neighbors

    def remove_edge(self, label_from, label_to):
        """
        delete new edge in the graph
        :param label_from: node the edge out from
        :param label_to: node the edge come into
        :return:
        """
        if label_from not in self.__nodes:
            raise ValueError(f"there is no node with label {label_from}")
        if label_to not in self.__nodes:
            raise ValueError(f"there is no node with label {label_to}")
        if label_to in self.__adjacency_list_out[label_from]:
            del self.__adjacency_list_out[label_from][label_to]
            del self.__adjacency_list_in[label_to][label_from]
        # if self.__matrix_neighbors is None or label_from not in self.__nodes:
        #     raise ValueError(f"there is no node with label {label_from}")
        # if label_to not in self.__nodes:
        #     raise ValueError(f"there is no node with label {label_to}")
        # self.__matrix_neighbors[self.__nodes[label_from].get_id(), self.__nodes[label_to].get_id()] = 0

    def remove_node(self, label):
        """
        remove node in the graph
        :param label: the value of the node to remove
        :return: None
        """
        if label not in self.__nodes:
            raise ValueError(f"there is no node with label {label}")
        else:
            if label in self.__adjacency_list_out:
                for lab in self.__adjacency_list_out[label].keys():
                    del self.__adjacency_list_in[lab][label]
                del self.__adjacency_list_out[label]
                # self.__adjacency_list_out.pop(label)
            if label in self.__adjacency_list_in:
                for lab in self.__adjacency_list_in[label].keys():
                    del self.__adjacency_list_out[lab][label]
                del self.__adjacency_list_in[label]
                # self.__adjacency_list_in.pop(label)
            # np.insert(self.__matrix_neighbors, self.__nodes[label].get_id(), 0, axis=0)
            # np.insert(self.__matrix_neighbors, self.__nodes[label].get_id(), 0, axis=1)
            self.__nodes.pop(label)

    def get_nodes(self, way=2):
        """
        return the nodes according to the way param
        :param way: 0 - return list of the labels
                    1 - return list of the nodes object
                    2 - return dictionary of the labels and the nodes they represent
        :return: according to way param
        """
        match way:
            case 0:
                return list(self.__nodes.keys())
            case 1:
                return list(self.__nodes.values())
            case 2:
                return self.__nodes
        # if way == 0:
        #     return self.__nodes.keys()
        # elif way == 1:
        #     return self.__nodes.values()
        # elif way == 2:
        #     return self.__nodes

    def get_node(self, label):
        """
        the node object with the given value
        :param label: the value of the node to return
        :return: the node object with the given value
        """
        return self.__nodes[label]

    def get_edges(self) -> set[tuple]:
        """
        :return: set of tuples of the edges in the graph - (node src, node dest, weight)
        """
        edges = set()
        for n_from in self.__adjacency_list_out:
            for n_to, weight in self.__adjacency_list_out[n_from].items():
                edges.add((n_from, n_to, weight))
        return edges

    def graph_reverse(self):
        """
        Do graph transpose
        :return: the reverse of this graph
        """
        g_reverse = DirectedGraph()
        g_reverse.__nodes = self.__nodes
        g_reverse.__adjacency_list_out = self.__adjacency_list_in
        g_reverse.__adjacency_list_in = self.__adjacency_list_out
        return g_reverse

    def sort(self, f, reverse):
        """
        sort the nodes on the graph by given sort function
        :param reverse: True if reverse the sorted else False
        :param f: lambda for sort key
        :return: None
        """
        self.__nodes = dict(sorted(self.__nodes.items(), key=f, reverse=reverse))


class UndirectedGraph(DirectedGraph):
    """
       This class represents an undirected weighted graph.
       """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def add_edge(self, label1, label2, weight=1):
        """
        create new edge in the graph
        :param label1: node 1
        :param label2: node 2
        :param weight: the weight of the edge
        :return:
        """
        super(UndirectedGraph, self).add_edge(label1, label2, weight)
        super(UndirectedGraph, self).add_edge(label2, label1, weight)

    def remove_edge(self, label1, label2):
        """
        delete new edge in the graph
        :param label1: node 1
        :param label2: node 2
        :return: None
        """
        super(UndirectedGraph, self).remove_edge(label1, label2)
        super(UndirectedGraph, self).remove_edge(label2, label1)

    def get_edges(self) -> set[tuple]:
        edges = super().get_edges()
        u_edges = set()
        for edge in edges:
            if (edge[1], edge[0], edge[2]) not in u_edges:
                u_edges.add(edge)
        return u_edges
