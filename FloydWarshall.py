def floyd_warshall_with_paths(graph):
    # Number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix and predecessor matrix
    dist = [row[:] for row in graph]
    pred = [[None if graph[i][j] == float('inf') else i for j in range(V)] for i in range(V)]

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
