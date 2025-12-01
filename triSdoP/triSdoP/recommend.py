from centrality import degree_centrality, closeness_centrality
from pagerank import pagerank
from community import label_propagation

def recommend_friends(graph, node,
                      w_mutual=1.0,
                      w_degree=0.2,
                      w_closeness=0.3,
                      w_pagerank=0.5,
                      community_bonus=1.0,
                      top_k=None):
    """
    Recommend friends for `node` using:
      - mutual friends (friends-of-friends)
      - degree centrality
      - closeness centrality
      - PageRank
      - community bonus
    """

    if node not in graph.adj_list:
        return []

    neighbors = set(graph.adj_list[node])

    # --- 1) Mutual friends feature -----------------
    scores = {}

    for friend in neighbors:
        for fof in graph.adj_list[friend]:
            if fof == node or fof in neighbors:
                continue
            scores[fof] = scores.get(fof, 0.0) + w_mutual

    if not scores:
        return []

    # --- 2) Global metrics -------------------------
    deg = degree_centrality(graph)          # {node: value}
    close = closeness_centrality(graph)     # {node: value}
    pr = pagerank(graph)                    # {node: value}

    for cand in scores:
        scores[cand] += w_degree * deg.get(cand, 0)
        scores[cand] += w_closeness * close.get(cand, 0)
        scores[cand] += w_pagerank * pr.get(cand, 0)

    # --- 3) Community bonus ------------------------
    communities = label_propagation(graph)
    comm_label = {}

    # label_propagation may return either a dict (label -> members)
    # or a list of member lists. Support both for backward compatibility.
    if isinstance(communities, dict):
        for idx, (lbl, members) in enumerate(communities.items()):
            for u in members:
                comm_label[u] = lbl
    else:
        for idx, comm in enumerate(communities):
            for u in comm:
                comm_label[u] = idx

    node_comm = comm_label.get(node)

    if node_comm is not None:
        for cand in scores:
            if comm_label.get(cand) == node_comm:
                scores[cand] += community_bonus

    # --- 4) Return sorted results -------------------
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    if top_k is not None:
        return ranked[:top_k]
    return ranked
