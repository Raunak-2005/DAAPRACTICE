import random

def max_cut(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Randomly assign each vertex to one of two sets (0 or 1)
    partition = {v: random.choice([0, 1]) for v in range(V)}
    
    # Count the number of edges that are cut
    cut_edges = 0
    for u in range(V):
        for v in graph[u]:
            if partition[u] != partition[v]:  # If u and v are in different sets
                cut_edges += 1
    
    # Each edge is counted twice (u-v and v-u), so divide by 2 to get the actual cut size
    cut_edges //= 2
    
    # Return the partition and the number of cut edges
    return partition, cut_edges

# Example graph: adjacency list representation
graph = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2]
}

# Running the Max Cut approximation algorithm
partition, cut_edges = max_cut(graph)

# Output the result
print("Partition of vertices:", partition)
print("Number of edges in the cut:", cut_edges)
