# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix as a copy of the graph
    dist = [row[:] for row in graph]

    # Apply the Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # If a shorter path is found through vertex k, update dist[i][j]
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
# Graph represented as an adjacency matrix
# graph[i][j] represents the weight of the edge from i to j, 
# and infinity (float('inf')) represents no direct edge.
graph = [
    [0, 3, float('inf'), float('inf'), float('inf')],
    [3, 0, 1, float('inf'), float('inf')],
    [float('inf'), 1, 0, 7, float('inf')],
    [float('inf'), float('inf'), 7, 0, 2],
    [float('inf'), float('inf'), float('inf'), 2, 0]
]

# Run Floyd-Warshall
dist = floyd_warshall(graph)

# Print the shortest distance matrix
for row in dist:
    print(row)
