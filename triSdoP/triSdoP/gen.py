# import random
# import string

# def generate_random_input(filename="input.txt", min_nodes=3, max_nodes=100000, max_edges=20000):
#     # Random number of nodes
#     n = random.randint(min_nodes, max_nodes)
    
#     # Generate unique node names (1-2 letters)
#     nodes = random.sample(list(string.ascii_lowercase), n)
    
#     # Random number of edges (at most n*(n-1)/2)
#     max_possible_edges = n*(n-1)//2
#     m = random.randint(0, min(max_edges, max_possible_edges))
    
#     edges = set()
#     while len(edges) < m:
#         u, v = random.sample(nodes, 2)
#         edge = tuple(sorted((u,v)))
#         edges.add(edge)
    
#     # Write to file
#     with open(filename, "w") as f:
#         f.write(f"{n}\n")
#         for node in nodes:
#             f.write(f"{node}\n")
#         f.write(f"{m}\n")
#         for u,v in edges:
#             f.write(f"{u} {v}\n")
    
#     print(f"Random input generated in {filename}")
#     print(f"Nodes ({n}): {', '.join(nodes)}")
#     print(f"Edges ({m}): {', '.join([f'{u}-{v}' for u,v in edges])}")

# if __name__ == "__main__":
#     generate_random_input()




import random
import string

def generate_node_names(n):
    """
    Generate n unique node names using letters a-z, then aa, ab, etc.
    """
    names = []
    i = 0
    while len(names) < n:
        name = ''
        x = i
        while True:
            name = string.ascii_lowercase[x % 26] + name
            x = x // 26 - 1
            if x < 0:
                break
        names.append(name)
        i += 1
    return names

def generate_random_input(filename="input.txt", min_nodes=3, max_nodes=50, max_edges=100):
    # Random number of nodes
    n = random.randint(min_nodes, max_nodes)
    
    # Generate unique node names
    nodes = generate_node_names(n)
    
    # Maximum possible edges
    max_possible_edges = n*(n-1)//2
    m = random.randint(0, min(max_edges, max_possible_edges))
    
    # Generate unique edges
    edges = set()
    while len(edges) < m:
        u, v = random.sample(nodes, 2)
        edge = tuple(sorted((u, v)))
        edges.add(edge)
    
    # Write to file
    with open(filename, "w") as f:
        f.write(f"{n}\n")
        for node in nodes:
            f.write(f"{node}\n")
        f.write(f"{m}\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")
    
    print(f"Random input generated in {filename}")
    print(f"Nodes ({n}): {', '.join(nodes[:min(20, n)])}{'...' if n > 20 else ''}")
    print(f"Edges ({m}): {', '.join([f'{u}-{v}' for u, v in list(edges)[:min(20, m)]])}{'...' if m > 20 else ''}")

if __name__ == "__main__":
    generate_random_input()
