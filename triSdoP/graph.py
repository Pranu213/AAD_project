# graph.py
from collections import defaultdict
from union_find import UnionFind

class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    # Add a node
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    # Add an undirected edge
    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Get neighbors of a node
    def get_neighbors(self, node):
        return self.adj_list[node]

    # Return list of nodes
    def get_nodes(self):
        return list(self.adj_list.keys())

    # Print adjacency list
    def print_graph(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

    # Connected components using Union-Find
    def connected_components(self):
        uf = UnionFind(list(self.adj_list.keys()))

        for u in self.adj_list:
            for v in self.adj_list[u]:
                uf.union(u, v)

        groups = defaultdict(list)
        for node in self.adj_list:
            parent = uf.find(node)
            groups[parent].append(node)

        # Return a mapping from representative (root) to list of members
        return groups
