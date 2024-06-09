
def get_bridges(graph):
    # Initialize a visited array and a parent array
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    
    # Initialize the number of bridges
    bridges = 0
    
    # Iterate over the vertices
    for vertex in range(len(graph)):
        # Check if the vertex has been visited
        if not visited[vertex]:
            # Recursively search the graph
            bridges += recursive_search(graph, visited, parent, vertex)
    
    return bridges

def recursive_search(graph, visited, parent, vertex):
    # Mark the current vertex as visited
    visited[vertex] = True
    
    # Iterate over the neighbors of the current vertex
    for neighbor in graph[vertex]:
        # Check if the neighbor has not been visited
        if not visited[neighbor]:
            # Recursively search the graph
            recursive_search(graph, visited, parent, neighbor)
            # Update the parent array
            parent[neighbor] = vertex
    
    # Return the number of bridges
    return len([neighbor for neighbor in graph[vertex] if parent[neighbor] != vertex])

