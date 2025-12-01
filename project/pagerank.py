# pagerank.py

def pagerank(graph, damping=0.85, max_iter=100, tol=1e-6):
    nodes = list(graph.adj_list.keys())
    N = len(nodes)

    # Equal initial rank
    rank = {node: 1 / N for node in nodes}

    for _ in range(max_iter):
        new_rank = {node: (1 - damping) / N for node in nodes}

        for node in nodes:
            neighbors = graph.adj_list[node]

            if len(neighbors) == 0:
                continue

            share = rank[node] / len(neighbors)

            for nbr in neighbors:
                new_rank[nbr] += damping * share

        diff = sum(abs(new_rank[n] - rank[n]) for n in nodes)
        if diff < tol:
            break

        rank = new_rank

    return rank
