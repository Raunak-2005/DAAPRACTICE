import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.d = float('inf')  # Distance initialized to infinity
        self.pd = None         # Parent node for path reconstruction

class Graph:
    def __init__(self):
        self.E = []  # List of edges
        self.V = []  # List of nodes
        self.adj = {}  # Adjacency list

def Relax(u, v, w):
    """Relax operation to update the shortest path estimate."""
    if u.d + w < v.d:
        v.d = u.d + w
        v.pd = u

def dijkstra(G, start):
    """Dijkstra's algorithm implementation."""
    start.d = 0  # Distance to the starting node is 0

    # Priority queue to store (distance, node)
    pq = []
    heapq.heappush(pq, (start.d, start))

    while pq:
        current_distance, u = heapq.heappop(pq)

        # If the current distance is greater than the recorded one, skip
        if current_distance > u.d:
            continue

        # Relax edges of u
        for v_value, weight in G.adj[u.value]:
            v = next(node for node in G.V if node.value == v_value)  # Find the actual node object
            Relax(u, v, weight)
            heapq.heappush(pq, (v.d, v))

# Graph initialization
G = Graph()
val = [1, 2, 3, 4]  # Node values
Edges = [(1, 2, 10), (1, 4, 15), (2, 3, 15), (3, 4, 20)]  # (u, v, weight)
Nodes = [Node(x) for x in val]

for i in Nodes:
    G.V.append(i)
    G.adj[i.value] = []  # Initialize adjacency list for each node

for u, v, w in Edges:
    G.E.append((u, v, w))
    G.adj[u].append((v, w))  # Add edge to adjacency list (directed)
    G.adj[v].append((u, w))  # For undirected graph

# Run Dijkstra's algorithm
start_node = next(node for node in G.V if node.value == 1)
dijkstra(G, start_node)

# Print shortest distances and paths
print("Node\tDistance from Start\tPath")
for node in G.V:
    # Reconstruct the path
    path = []
    current = node
    while current:
        path.append(current.value)
        current = current.pd
    path.reverse()
    print(f"{node.value}\t{node.d}\t\t\t{path}")
