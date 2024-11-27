def vertex_cover_approx(graph):
    # Initialize the vertex cover set
    vertex_cover = set()
    
    # Create a copy of the graph (adjacency list)
    edges = set()
    for u in graph:
        for v in graph[u]:
            if u < v:  # To avoid duplicates, consider each edge only once
                edges.add((u, v))
    
    # Greedily select edges and add both vertices to the vertex cover
    while edges:
        # Pick an arbitrary edge (u, v)
        u, v = edges.pop()
        
        # Add both u and v to the vertex cover
        vertex_cover.add(u)
        vertex_cover.add(v)
        
        # Remove all edges incident to u or v
        edges = {e for e in edges if u not in e and v not in e}
    
    return vertex_cover

# Example usage:
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

vertex_cover = vertex_cover_approx(graph)
print(f"Vertex Cover: {vertex_cover}")
