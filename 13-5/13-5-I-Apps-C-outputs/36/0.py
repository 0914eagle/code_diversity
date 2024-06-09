
def solve(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the pigs and their current vertices
    pig_vertices = {pig: vertex for pig, vertex in enumerate(pigs)}
    
    # Initialize a set to keep track of the vertices that are safe for the pigs to escape to
    safe_vertices = set()
    
    # Loop through each pig and find the safe vertices they can escape to
    for pig in range(P):
        current_vertex = pig_vertices[pig]
        safe_vertices.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in safe_vertices:
                safe_vertices.add(neighbor)
    
    # Count the number of wolves that need to be removed
    num_wolves_to_remove = 0
    for vertex in range(V):
        if vertex not in safe_vertices and vertex in pig_vertices.values():
            num_wolves_to_remove += 1
    
    return num_wolves_to_remove

