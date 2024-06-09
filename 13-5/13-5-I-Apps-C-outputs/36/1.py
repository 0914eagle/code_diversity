
def get_min_wolves_to_remove(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the pigs and their current vertices
    pig_vertices = {pig: vertex for pig, vertex in enumerate(pigs)}
    
    # Initialize a set to keep track of the vertices that are not occupied by a wolf
    safe_vertices = set(range(V)) - set(pigs)
    
    # Initialize a variable to keep track of the minimum number of wolves to remove
    min_wolves = 0
    
    # Iterate until all pigs can escape
    while any(vertex in safe_vertices for vertex in pig_vertices.values()):
        # Find the pig that is closest to a safe vertex
        closest_pig = None
        closest_distance = float('inf')
        for pig, vertex in pig_vertices.items():
            if vertex in safe_vertices:
                continue
            distance = len(graph[vertex])
            if distance < closest_distance:
                closest_distance = distance
                closest_pig = pig
        
        # Remove the wolf that is currently occupying the vertex of the closest pig
        wolf_vertex = pig_vertices[closest_pig]
        safe_vertices.add(wolf_vertex)
        min_wolves += 1
        
        # Move the pig to a safe vertex
        for vertex in graph[wolf_vertex]:
            if vertex in safe_vertices:
                pig_vertices[closest_pig] = vertex
                break
    
    return min_wolves

