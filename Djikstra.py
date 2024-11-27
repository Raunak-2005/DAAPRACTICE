import heapq

class Graph:
    def __init__(self):
        # Dictionary to store the graph as an adjacency list
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        """Adds a weighted edge between vertices u and v."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # For undirected graph; remove for directed graphs

    def dijkstra(self, start):
        """Finds shortest paths from `start` to all other nodes and tracks the path."""
        # Priority queue to store (distance, node)
        pq = [(0, start)]
        # Dictionary to store the shortest distances from start to each node
        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        # Dictionary to store the previous node for each node (for path reconstruction)
        previous_nodes = {node: None for node in self.adj_list}
        # Set to keep track of visited nodes
        visited = set()

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous_nodes

    def get_path(self, start, end, previous_nodes):
        """Reconstructs the shortest path from start to end using the previous_nodes dictionary."""
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()
        return path if path[0] == start else []

# Example Usage
g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 6)
g.add_edge(3, 4, 3)

start_node = 1
distances, previous_nodes = g.dijkstra(start_node)

# Print shortest distances and paths to each node
for node in g.adj_list:
    if distances[node] < float('inf'):
        path = g.get_path(start_node, node, previous_nodes)
        print(f"Shortest distance from {start_node} to {node}: {distances[node]}, Path: {path}")
