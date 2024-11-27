def floyd_warshall_with_paths(graph):
    # Number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix as a copy of the graph
    dist = [row[:] for row in graph]

    # Initialize the predecessor matrix with None for all pairs
    pred = [[None for _ in range(V)] for _ in range(V)]

    # Set the predecessors for direct edges
    for i in range(V):
        for j in range(V):
            if graph[i][j] != float('inf') and i != j:  # Direct edge exists
                pred[i][j] = i

    # Apply the Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # If a shorter path is found through vertex k, update dist[i][j]
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def print_path(pred, start, end):
    """Recursively print the path from start to end using the predecessor matrix."""
    if start == end:
        print(start, end=" ")
    elif pred[start][end] is None:
        print(f"No path from {start} to {end}")
    else:
        print_path(pred, start, pred[start][end])
        print(end, end=" ")

# Example usage:
graph = [
    [0, 3, float('inf'), float('inf'), float('inf')],
    [3, 0, 1, float('inf'), float('inf')],
    [float('inf'), 1, 0, 7, float('inf')],
    [float('inf'), float('inf'), 7, 0, 2],
    [float('inf'), float('inf'), float('inf'), 2, 0]
]

# Run Floyd-Warshall with paths
dist, pred = floyd_warshall_with_paths(graph)

# Print the shortest distance matrix
print("Shortest distance matrix:")
for row in dist:
    print(row)

# Print all paths
print("\nPaths between all pairs of vertices:")
V = len(graph)
for i in range(V):
    for j in range(V):
        print(f"Path from {i} to {j}: ", end="")
        print_path(pred, i, j)
        print()
