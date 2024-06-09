
def get_bridges(graph):
    # Initialize a visited array and a parent array
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    
    # Initialize the number of bridges
    bridges = 0
    
    # Iterate over the vertices
    for vertex in range(len(graph)):
        # If the vertex is not visited, do a DFS from that vertex
        if not visited[vertex]:
            dfs(graph, vertex, visited, parent)
    
    # Iterate over the edges
    for edge in graph:
        # If the edge is not a self-loop and the parent of the edge's destination is not the same as the parent of the edge's source, then the edge is a bridge
        if edge[0] != edge[1] and parent[edge[1]] != parent[edge[0]]:
            bridges += 1
    
    return bridges

def dfs(graph, vertex, visited, parent):
    # Mark the current vertex as visited
    visited[vertex] = True
    
    # Iterate over the neighbors of the current vertex
    for neighbor in graph[vertex]:
        # If the neighbor is not visited, do a DFS from that neighbor
        if not visited[neighbor]:
            parent[neighbor] = vertex
            dfs(graph, neighbor, visited, parent)

