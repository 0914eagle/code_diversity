
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
    a = 0
    b = 0
    c = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the distance between the two vertices is 2, they are connected by an edge
            if len(graph[i] & graph[j]) == 1:
                # If the number of edges is greater than the current maximum, update the maximum and the corresponding vertices
                if max_edges < 3:
                    max_edges = 3
                    a = i
                    b = j
                    c = 0
                # If the number of edges is equal to the current maximum, update the corresponding vertices
                elif max_edges == 3:
                    a = i
                    b = j
                    c = 0
    
    return [max_edges, a, b, c]

