
def solve(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a set to store the vertices occupied by pigs
    pig_vertices = set(pigs)
    
    # Initialize a set to store the vertices occupied by wolves
    wolf_vertices = set(range(V)) - pig_vertices
    
    # Initialize a queue to store the vertices to be visited
    queue = []
    
    # Enqueue the vertices occupied by pigs
    for pig in pig_vertices:
        queue.append(pig)
    
    # Initialize a variable to store the minimum number of wolves to remove
    min_wolves = 0
    
    while queue:
        # Dequeue a vertex
        vertex = queue.pop(0)
        
        # If the vertex is a leaf vertex, it can be removed
        if len(graph[vertex]) == 1:
            min_wolves += 1
            continue
        
        # If the vertex is occupied by a wolf, it cannot be removed
        if vertex in wolf_vertices:
            continue
        
        # Enqueue the neighbors of the vertex
        for neighbor in graph[vertex]:
            queue.append(neighbor)
    
    return min_wolves

