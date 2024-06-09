
def solve(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize variables to store the maximum number of edges and the vertices with the maximum number of edges
    max_edges = 0
    max_vertices = []
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Initialize a set to store the edges in the path between i and j
            path = set()
            
            # Add the edge between i and j to the path
            path.add((i, j))
            
            # Iterate over the neighbors of i and j
            for neighbor in graph[i]:
                if neighbor != j:
                    path.update(graph[neighbor])
            for neighbor in graph[j]:
                if neighbor != i:
                    path.update(graph[neighbor])
                
            # If the number of edges in the path is greater than the maximum number of edges, update the maximum number of edges and the vertices with the maximum number of edges
            if len(path) > max_edges:
                max_edges = len(path)
                max_vertices = [i, j]
    
    return max_edges, max_vertices

