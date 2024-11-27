import math

# Function to calculate the Euclidean distance between two points
def distance(v1, v2):
    return math.sqrt((v2[0] - v1[0])*2 + (v2[1] - v1[1])*2)

# Nearest Neighbor TSP algorithm
def tsp_nearest_neighbor(points):
    n = len(points)
    visited = [False] * n
    tour = []
    total_distance = 0

    # Start from the first city (index 0)
    current_city = 0
    visited[current_city] = True
    tour.append(current_city)

    for _ in range(n - 1):
        nearest_city = None
        nearest_distance = float('inf')

        # Find the nearest unvisited city
        for i in range(n):
            if not visited[i]:
                dist = distance(points[current_city], points[i])
                if dist < nearest_distance:
                    nearest_distance = dist
                    nearest_city = i

        # Visit the nearest city
        visited[nearest_city] = True
        tour.append(nearest_city)
        total_distance += nearest_distance
        current_city = nearest_city

    # Return to the starting city
    total_distance += distance(points[current_city], points[tour[0]])
    tour.append(tour[0])  # Complete the cycle

    return tour, total_distance

# Example usage
if __name__ == "_main_":
    # Define the points (cities) as 2D coordinates
    points = [
        (0, 0),  # City 0
        (2, 2),  # City 1
        (2, 0),  # City 2
        (3, 3),  # City 3
        (5, 2),  # City 4
    ]

    # Find the TSP tour using the nearest neighbor heuristic
    tour, total_dist = tsp_nearest_neighbor(points)
    
    # Output the tour and total distance
    print("TSP Tour:", tour)
    print("Total Distance:", total_dist)