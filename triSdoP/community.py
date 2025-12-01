# community.py
import random

def label_propagation(graph):
    labels = {node: node for node in graph.adj_list}
    nodes = list(graph.adj_list.keys())

    for _ in range(10):  # iterations
        random.shuffle(nodes)

        for node in nodes:
            if not graph.adj_list[node]:
                continue

            # Count neighbor labels
            freq = {}
            for nbr in graph.adj_list[node]:
                lbl = labels[nbr]
                freq[lbl] = freq.get(lbl, 0) + 1

            # Pick label with highest frequency
            labels[node] = max(freq, key=freq.get)

    # Group nodes by label
    communities = {}
    for node, lbl in labels.items():
        communities.setdefault(lbl, []).append(node)

    # Return mapping from label to members
    return communities
