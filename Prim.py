import heapq

def prim(graph):
    # Initialize variables
    V = len(graph)
    mst = []  # To store edges in the MST
    visited = [False] * V  # To track visited vertices
    min_heap = [(0, 0)]  # Min heap: (weight, vertex), start with vertex 0

    total_cost = 0  # To store the total cost of MST
    
    while min_heap:
        # Extract the vertex with the minimum edge weight
        weight, u = heapq.heappop(min_heap)
        
        # If the vertex has already been visited, skip it
        if visited[u]:
            continue

        # Mark the vertex as visited
        visited[u] = True
        total_cost += weight
        
        # Add the edge to the MST
        if weight != 0:  # Skip the starting vertex (with weight 0)
            mst.append((prev, u, weight))
        
        # Update adjacent vertices
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                prev = u  # Track the previous vertex for the edge

    return mst, total_cost

# Example usage:
# Graph represented as an adjacency list: (vertex, weight)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)]
}

mst, cost = prim(graph)
print(f"Minimum Spanning Tree: {mst}")
print(f"Total cost: {cost}")
