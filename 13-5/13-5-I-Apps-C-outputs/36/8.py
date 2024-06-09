
def solve(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the number of pigs on each vertex
    pig_count = [0] * V
    for pig in pigs:
        pig_count[pig] += 1
    
    # Initialize a set to keep track of the vertices with at least one pig
    pig_vertices = set()
    for pig in pigs:
        pig_vertices.add(pig)
    
    # Initialize a set to keep track of the vertices with at least one wolf
    wolf_vertices = set()
    
    # Loop through each vertex and check if it is a leaf vertex
    for vertex in range(V):
        if len(graph[vertex]) == 1 and vertex not in pig_vertices:
            # If the vertex is a leaf vertex and there is no pig on it, it is a wolf vertex
            wolf_vertices.add(vertex)
    
    # Initialize a variable to keep track of the minimum number of wolves to remove
    min_wolves = 0
    
    # Loop through each vertex and check if it is a pig vertex
    for vertex in range(V):
        if vertex in pig_vertices:
            # If the vertex is a pig vertex, check if it is connected to a wolf vertex
            for neighbor in graph[vertex]:
                if neighbor in wolf_vertices:
                    # If the vertex is connected to a wolf vertex, remove the wolf vertex and update the minimum number of wolves to remove
                    wolf_vertices.remove(neighbor)
                    min_wolves += 1
                    break
    
    return min_wolves

