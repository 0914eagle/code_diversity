
def count_simple_loops(m, n, connections):
    # Initialize a graph with m nodes and n edges
    graph = [[] for _ in range(m)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
    
    # Find all simple loops in the graph
    loops = set()
    for node in range(m):
        for neighbor in graph[node]:
            if neighbor != node:
                loops.add(tuple(sorted([node, neighbor])))
    
    # Count the number of unique simple loops
    return len(loops)

