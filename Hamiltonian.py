import math

# Function to calculate Euclidean distance between two points
def distance(v1, v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

# Nearest Neighbor Approximation Algorithm for Hamiltonian Cycle
def nearest_neighbor(graph, start):
    n = len(graph)
    visited = [False] * n
    cycle = [start]
    visited[start] = True
    current_vertex = start
    
    # Loop to visit all vertices
    for _ in range(n - 1):
        nearest_vertex = -1
        min_dist = float('inf')
        
        # Find the nearest unvisited vertex
        for neighbor in range(n):
            if not visited[neighbor]:
                dist = distance(graph[current_vertex], graph[neighbor])
                if dist < min_dist:
                    min_dist = dist
                    nearest_vertex = neighbor
        
        # Move to the nearest vertex
        visited[nearest_vertex] = True
        cycle.append(nearest_vertex)
        current_vertex = nearest_vertex
    
    # Returning to the start vertex to complete the cycle
    cycle.append(start)
    
    return cycle

# Function to calculate the total distance of the cycle
def total_distance(graph, cycle):
    total_dist = 0
    for i in range(len(cycle) - 1):
        total_dist += distance(graph[cycle[i]], graph[cycle[i + 1]])
    return total_dist

# Example usage
if __name__ == "__main__":
    # Define graph as a list of 2D coordinates representing vertices
    graph = [(0, 0), (2, 2), (3, 1), (5, 3), (6, 1)]
    
    # Start from vertex 0
    start_vertex = 0
    
    # Get the Hamiltonian cycle using nearest neighbor algorithm
    cycle = nearest_neighbor(graph, start_vertex)
    
    # Calculate the total distance of the cycle
    cycle_distance = total_distance(graph, cycle)
    
    # Output the cycle and its total distance
    print("Hamiltonian Cycle:", cycle)
    print("Total Distance of the Cycle:", cycle_distance)
