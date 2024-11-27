# Disjoint Set Union-Find (with path compression and union by rank)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank is used to keep the tree flat

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])  # Sorting by the third element (edge weight)
    
    uf = UnionFind(n)
    mst = []  # List to store the edges of the MST
    mst_weight = 0  # Variable to store the total weight of the MST

    # Step 2: Process each edge in sorted order
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # If u and v are in different components
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
            if len(mst) == n - 1:  # Stop once we have n-1 edges
                break

    return mst, mst_weight

# Example usage:
edges = [
    (0, 1, 2), (0, 3, 6), 
    (1, 2, 3), (1, 3, 8), 
    (2, 3, 7)
]
n = 4  # Number of vertices

mst, mst_weight = kruskal(n, edges)
print(f"Minimum Spanning Tree: {mst}")
print(f"Total weight of MST: {mst_weight}")
