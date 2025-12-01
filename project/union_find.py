class UnionFind:
    def __init__(self, nodes):
        self.parent = {v: v for v in nodes}
        self.rank = {v: 0 for v in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb:
            return

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

    def connected_components(self):
        comps = {}
        for node in self.parent:
            root = self.find(node)
            comps.setdefault(root, []).append(node)
        return list(comps.values())
