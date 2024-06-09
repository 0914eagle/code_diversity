
def is_tree(n, d, k):
    # Check if the input is valid
    if n < 1 or d < 1 or k < 1:
        return False
    
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]
    
    # Add edges to the graph
    for i in range(n - 1):
        # Choose two random vertices
        v1 = random.randint(0, n - 1)
        v2 = random.randint(0, n - 1)
        
        # Check if the vertices are not already connected and if the degree of the vertices is less than or equal to k
        if v1 != v2 and len(graph[v1]) + len(graph[v2]) <= k:
            graph[v1].append(v2)
            graph[v2].append(v1)
    
    # Check if the graph is connected
    visited = set()
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    
    # Check if the graph has diameter at most d
    diameter = 0
    for vertex in visited:
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                diameter = max(diameter, vertex - neighbor)
    
    return diameter <= d

