# recommend.py

from centrality import degree_centrality
from pagerank import pagerank
from community import label_propagation

def recommend_friends(graph, node,
                      w_mutual=1.0,
                      w_degree=0.2,
                      w_pagerank=0.5,
                      community_bonus=1.0):
    """
    Recommend friends for `node` using:
      - mutual friends (friends-of-friends)
      - degree centrality
      - PageRank
      - community (label propagation)
    """

    if node not in graph.adj_list:
        return []

    neighbors = set(graph.adj_list[node])

    # --- 1) Base score from mutual friends ---
    scores = {}

    for friend in neighbors:
        for fof in graph.adj_list[friend]:
            # skip self and existing direct neighbors
            if fof == node or fof in neighbors:
                continue

            # base score: mutual friend count
            scores[fof] = scores.get(fof, 0.0) + w_mutual

    if not scores:
        # No friends-of-friends → nothing to recommend
        return []

    # --- 2) Global signals: degree centrality & PageRank ---
    deg = degree_centrality(graph)       # {node: degree}
    pr = pagerank(graph)                 # {node: pagerank_score}

    for cand in scores:
        scores[cand] += w_degree * deg.get(cand, 0)
        scores[cand] += w_pagerank * pr.get(cand, 0.0)

    # --- 3) Communities (label propagation) ---
    communities = label_propagation(graph)  # [[nodes in comm1], [nodes in comm2], ...]
    comm_label = {}
    for idx, comm in enumerate(communities):
        for u in comm:
            comm_label[u] = idx

    node_comm = comm_label.get(node, None)

    if node_comm is not None:
        for cand in scores:
            if comm_label.get(cand) == node_comm:
                # same community → give bonus
                scores[cand] += community_bonus

    # --- 4) Sort by final score, descending ---
    return sorted(scores.items(), key=lambda x: -x[1])