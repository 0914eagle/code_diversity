
def solve(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize three variables to store the maximum number of edges and the corresponding vertices
    max_edges = 0
    a, b, c = 0, 0, 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the vertices are not connected, skip this pair
            if j not in graph[i]:
                continue
            
            # Initialize a set to store the edges between the two vertices
            edges_between = set()
            
            # Add the edge between the two vertices to the set
            edges_between.add((i, j))
            
            # Add the edges from the first vertex to the set
            for edge in graph[i]:
                if edge != j:
                    edges_between.add((i, edge))
            
            # Add the edges from the second vertex to the set
            for edge in graph[j]:
                if edge != i:
                    edges_between.add((j, edge))
            
            # If the number of edges is greater than the maximum number of edges, update the maximum number of edges and the corresponding vertices
            if len(edges_between) > max_edges:
                max_edges = len(edges_between)
                a, b, c = i, j, 0
    
    return max_edges, a, b, c

