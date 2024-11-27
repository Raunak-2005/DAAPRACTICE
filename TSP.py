import math
import heapq

# Function to calculate Euclidean distance between two points
def distance(v1, v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

# Function to build a minimum spanning tree (MST) using Prim's algorithm
def build_mst(graph):
    n = len(graph)
    mst = [[] for _ in range(n)]  # List of edges in the MST
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex) -> start from vertex 0
    total_weight = 0

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        if visited[vertex]:
            continue
        visited[vertex] = True
        total_weight += weight

        # Add edges to the MST
        for neighbor in range(n):
            if not visited[neighbor]:
                dist = distance(graph[vertex], graph[neighbor])
                heapq.heappush(min_heap, (dist, neighbor))
                mst[vertex].append(neighbor)
                mst[neighbor].append(vertex)

    return mst

# Depth-first search (DFS) to traverse the MST and form a TSP tour
def dfs(mst, vertex, visited, tour):
    visited[vertex] = True
    tour.append(vertex)

    for neighbor in mst[vertex]:
        if not visited[neighbor]:
            dfs(mst, neighbor, visited, tour)

# Function to calculate the total distance of a tour
def total_distance(graph, tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(graph[tour[i]], graph[tour[i + 1]])
    total_dist += distance(graph[tour[-1]], graph[tour[0]])  # Return to the starting point
    return total_dist

# Approximation algorithm for TSP using MST
def tsp_approximation(graph):
    # Step 1: Build the MST
    mst = build_mst(graph)

    # Step 2: Perform DFS to get the TSP tour
    n = len(graph)
    visited = [False] * n
    tour = []
    dfs(mst, 0, visited, tour)

    # Step 3: Calculate the total distance of the tour
    total_dist = total_distance(graph, tour)
    
    return tour, total_dist

# Example usage
if __name__ == "__main__":
    # Define graph as a list of 2D coordinates representing vertices
    graph = [(0, 0), (2, 2), (3, 1), (5, 3), (6, 1)]
    
    # Get the TSP approximation using the MST-based algorithm
    tour, total_dist = tsp_approximation(graph)
    
    # Output the tour and its total distance
    print("TSP Tour:", tour)
    print("Total Distance of the TSP Approximation:", total_dist)
