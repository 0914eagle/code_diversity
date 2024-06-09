
def get_bridges(graph):
    # Initialize a visited array and a parent array
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    
    # Initialize the number of bridges
    bridges = 0
    
    # Iterate through all vertices
    for vertex in range(len(graph)):
        # If the vertex is not visited, then recur through it
        if not visited[vertex]:
            bridges += recur_through_vertex(graph, vertex, visited, parent)
    
    return bridges

def recur_through_vertex(graph, vertex, visited, parent):
    # Mark the current vertex as visited
    visited[vertex] = True
    
    # Iterate through the adjacent vertices
    for adjacent in graph[vertex]:
        # If the adjacent vertex is not visited, then recur through it
        if not visited[adjacent]:
            parent[adjacent] = vertex
            bridges += recur_through_vertex(graph, adjacent, visited, parent)
    
    # If the vertex is not a leaf node, then it is a bridge
    if parent[vertex] != -1:
        bridges += 1
    
    return bridges

