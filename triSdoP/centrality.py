# centrality.py
from collections import deque

def degree_centrality(graph):
    return {node: len(graph.adj_list[node]) for node in graph.adj_list}

def closeness_centrality(graph):
    nodes = list(graph.adj_list.keys())
    closeness = {}

    def bfs(src):
        dist = {node: float('inf') for node in nodes}
        dist[src] = 0
        q = deque([src])

        while q:
            u = q.popleft()
            for v in graph.adj_list[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    q.append(v)

        return dist

    for node in nodes:
        dist = bfs(node)
        reachable = [d for d in dist.values() if d < float('inf')]
        closeness[node] = (len(reachable)-1) / sum(reachable) if len(reachable) > 1 else 0

    return closeness
