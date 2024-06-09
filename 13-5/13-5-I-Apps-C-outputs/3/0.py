
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given nodes and edges
    graph = {i: set() for i in range(n)}
    for u, v, c in edges:
        graph[u].add((v, c))
    
    # Initialize the flow graph with the given source and sink
    flow_graph = {s: set([(v, c) for v, c in graph[s]]), t: set()}
    
    # Initialize the maximum flow and the number of edges used
    max_flow = 0
    m_used = 0
    
    # While there is a path from the source to the sink in the flow graph
    while flow_graph[s]:
        # Find a path from the source to the sink in the flow graph
        path = []
        current = s
        while current != t:
            path.append(current)
            current = min(flow_graph[current], key=lambda x: x[1])[0]
        path.append(t)
        
        # Update the flow graph with the path
        flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            flow = min(flow, graph[u][(v, c)][1] - flow_graph[u][(v, c)])
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            flow_graph[u][(v, c)] -= flow
            flow_graph[v][(u, c)] += flow
        
        # Update the maximum flow and the number of edges used
        max_flow += flow
        m_used += len(path) - 1
    
    # Return the maximum flow and the number of edges used
    return max_flow, m_used

