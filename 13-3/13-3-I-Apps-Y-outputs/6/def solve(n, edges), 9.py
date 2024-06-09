
def solve(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize variables to store the maximum number of edges and the corresponding vertices
    max_edges = 0
    a, b, c = 0, 0, 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the vertices are not connected, skip this pair
            if j not in graph[i]:
                continue
            
            # Initialize a set to store the edges that are common to both paths
            common_edges = set()
            
            # Find the number of edges that are common to the paths from i to j and from j to i
            for k in graph[i]:
                if k in graph[j]:
                    common_edges.add((i, k))
                    common_edges.add((k, j))
            
            # If the number of common edges is greater than the current maximum, update the maximum and the corresponding vertices
            if len(common_edges) > max_edges:
                max_edges = len(common_edges)
                a, b, c = i, j, 0
    
    return max_edges, a, b, c

