
def count_simple_loops(m, n, connections):
    # Initialize a graph with m nodes and n edges
    graph = [[] for _ in range(m)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
    
    # Count the number of simple loops
    loops = 0
    for node in range(m):
        for neighbor in graph[node]:
            if neighbor != node:
                loops += 1
    
    return loops

