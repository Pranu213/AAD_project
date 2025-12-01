# main.py

from graph import Graph
from centrality import degree_centrality, closeness_centrality
from pagerank import pagerank
from community import label_propagation
from recommend import recommend_friends

print("\n=== GRAPH INPUT ===")

# Number of nodes
n = int(input("Enter number of nodes: "))

graph = Graph()

# Add nodes
print("\nEnter node names:")
nodes = []
for i in range(n):
    name = input(f"Node {i+1}: ").strip()
    nodes.append(name)
    graph.add_node(name)

# Number of edges
m = int(input("\nEnter number of edges: "))

# Add edges
print("\nEnter edges in 'u v' format:")
for i in range(m):
    u, v = input(f"Edge {i+1}: ").split()
    graph.add_edge(u, v)


# ----------------------------------------------------
# OUTPUTS
# ----------------------------------------------------

print("\n=== ADJACENCY LIST ===")
graph.print_graph()

# Neighbors of all nodes
print("\n=== Neighbors of All Nodes ===")
for node in graph.adj_list:
    neighbors = graph.get_neighbors(node)
    print(f"{node} → {', '.join(neighbors)}")

print("\n=== Connected Components (Union-Find) ===")
print(graph.connected_components())

print("\n=== Degree Centrality ===")
deg_cent = degree_centrality(graph)
print(deg_cent)

print("\n=== Closeness Centrality ===")
close_cent = closeness_centrality(graph)
print(close_cent)

print("\n=== PageRank ===")
pr = pagerank(graph)
print(pr)

print("\n=== Communities (Label Propagation) ===")
communities = label_propagation(graph)
print(communities)

print("\n=== Friend Recommendations for ALL Nodes ===")
for node in graph.adj_list:
    recs = recommend_friends(graph, node)
    formatted = [f"{n} ({score})" for n, score in recs]
    print(f"{node} → {formatted}")

print("\n=== DONE ===\n")
