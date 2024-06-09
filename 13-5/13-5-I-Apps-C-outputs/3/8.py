
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given edges
    graph = {i: [] for i in range(n)}
    for u, v, c in edges:
        graph[u].append((v, c))
    
    # Initialize the flow graph with the given source and sink
    flow_graph = {i: [] for i in range(n)}
    flow_graph[s].append((t, 0))
    
    # Initialize the maximum flow and the number of edges used
    max_flow = 0
    num_edges = 0
    
    # While there is a path from the source to the sink
    while True:
        # Find a path from the source to the sink
        path = []
        visited = set()
        queue = [(s, [s])]
        while queue:
            (u, path) = queue.pop(0)
            if u == t:
                break
            for v, c in graph[u]:
                if v not in visited and c > 0:
                    visited.add(v)
                    queue.append((v, path + [v]))
        
        # If there is no path from the source to the sink, stop
        if not path:
            break
        
        # Find the minimum capacity of the edges in the path
        min_capacity = float('inf')
        for u, v in zip(path, path[1:]):
            min_capacity = min(min_capacity, graph[u][v][1])
        
        # Add the flow to the flow graph
        for u, v in zip(path, path[1:]):
            flow_graph[u].append((v, graph[u][v][1]))
        flow_graph[s].append((t, min_capacity))
        
        # Update the maximum flow and the number of edges used
        max_flow += min_capacity
        num_edges += len(path) - 1
    
    # Return the maximum flow and the number of edges used
    return max_flow, num_edges

