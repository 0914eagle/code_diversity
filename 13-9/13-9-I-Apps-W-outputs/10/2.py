
def count_simple_loops(m, n, connections):
    # Initialize a graph with m nodes and n edges
    graph = [[] for _ in range(m)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
    
    # Count the number of simple loops
    loops = 0
    for i in range(m):
        for j in range(m):
            if i != j and graph[i] and graph[j] and graph[i][0] == graph[j][0]:
                loops += 1
    
    return loops

