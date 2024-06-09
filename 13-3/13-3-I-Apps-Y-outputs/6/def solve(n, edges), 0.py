
def solve(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize three variables to store the maximum number of edges and the vertices corresponding to the maximum number of edges
    max_edges = 0
    max_vertices = []
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Initialize a set to store the edges between the two vertices
            edge_set = set()
            
            # Add the edges between the two vertices to the set
            for edge in graph[i]:
                if edge in graph[j]:
                    edge_set.add(edge)
            
            # If the set of edges has more elements than the current maximum, update the maximum and the corresponding vertices
            if len(edge_set) > max_edges:
                max_edges = len(edge_set)
                max_vertices = [i, j]
    
    return max_edges, max_vertices

