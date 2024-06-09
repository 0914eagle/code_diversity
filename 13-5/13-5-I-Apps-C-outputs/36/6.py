
def solve(V, P, edges, initial_vertices):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the number of pigs on each vertex
    pig_count = {vertex: 0 for vertex in range(V)}
    for vertex in initial_vertices:
        pig_count[vertex] += 1
    
    # Initialize a set to keep track of the vertices that are safe for the pigs to escape to
    safe_vertices = set()
    
    # Iterate through each vertex in the graph
    for vertex in range(V):
        # If the vertex is not occupied by a wolf and has at least one edge, it is a safe vertex
        if pig_count[vertex] == 0 and len(graph[vertex]) > 0:
            safe_vertices.add(vertex)
    
    # Initialize a variable to keep track of the minimum number of wolves to remove
    min_wolves = 0
    
    # Iterate through each vertex in the graph
    for vertex in range(V):
        # If the vertex is occupied by a pig and there is at least one safe vertex that the pig can escape to, remove the wolf on that vertex
        if pig_count[vertex] > 0 and len(safe_vertices) > 0:
            min_wolves += 1
            pig_count[vertex] -= 1
            safe_vertices.remove(vertex)
    
    return min_wolves

