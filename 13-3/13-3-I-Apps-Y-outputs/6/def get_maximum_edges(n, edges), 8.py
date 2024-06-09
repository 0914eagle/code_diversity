
def get_maximum_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize three variables to store the answer
    max_edges = 0
    a = 0
    b = 0
    c = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the distance between the two vertices is 2, they are connected by an edge
            if len(graph[i] & graph[j]) == 1:
                # If the distance between the two vertices is 2 and the number of edges is greater than the current maximum, update the answer
                if max_edges < 2:
                    max_edges = 2
                    a = i
                    b = j
            
    # Return the answer
    return [max_edges, a, b]

