import math

# Function to calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Function to find the closest pair of points
def closest_pair(points):
    n = len(points)
    if n < 2:
        return None, float('inf')  # No pair exists if less than 2 points
    
    min_dist = float('inf')
    closest_pair = None
    
    # Brute-force O(n^2) approach
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_dist

# Example usage:
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
pair, dist = closest_pair(points)
print(f"Closest pair: {pair}")
print(f"Distance: {dist}")
