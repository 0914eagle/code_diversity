
def min_wolves_to_escape(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the pigs and their current vertices
    pig_vertices = {pig: vertex for pig, vertex in enumerate(pigs)}
    
    # Initialize a set to keep track of the vertices that are safe for the pigs to escape to
    safe_vertices = set()
    
    # Loop through each pig and their current vertex
    for pig, vertex in pig_vertices.items():
        # If the vertex is a leaf vertex, add it to the safe vertices set
        if len(graph[vertex]) == 1:
            safe_vertices.add(vertex)
        # Otherwise, find the safe vertices that the pig can move to
        else:
            for neighbor in graph[vertex]:
                if neighbor not in safe_vertices:
                    safe_vertices.add(neighbor)
    
    # Return the number of wolves that need to be removed to make all the pigs escape
    return V - len(safe_vertices)

