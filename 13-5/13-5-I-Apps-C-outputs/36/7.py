
def get_minimum_wolves(V, P, edges, initial_vertices):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the number of pigs and wolves on each vertex
    counts = [0] * V
    for vertex in initial_vertices:
        counts[vertex] += 1
    
    # Initialize a queue to keep track of the vertices to visit
    queue = []
    
    # Add the initial vertices occupied by pigs to the queue
    for vertex in initial_vertices:
        queue.append(vertex)
    
    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)
        
        # If the current vertex is a leaf vertex (connected to only one edge), return the current number of wolves
        if len(graph[vertex]) == 1:
            return counts[vertex] - 1
        
        # Otherwise, add the neighboring vertices to the queue
        for neighbor in graph[vertex]:
            if counts[neighbor] == 0:
                queue.append(neighbor)
                counts[neighbor] += 1
    
    # If all pigs cannot escape, return -1
    return -1

