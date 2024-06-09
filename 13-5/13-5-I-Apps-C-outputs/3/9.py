
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given edges
    graph = [[] for _ in range(n)]
    for u, v, c in edges:
        graph[u].append((v, c))
    
    # Initialize the maximum flow and the number of edges used
    max_flow = 0
    edges_used = 0
    
    # Initialize the source and sink nodes
    source = s
    sink = t
    
    # While there are still edges to be used
    while edges_used < m:
        # Find the minimum capacity of the edges leaving the source node
        min_capacity = float('inf')
        for v, c in graph[source]:
            if c < min_capacity:
                min_capacity = c
        
        # If the minimum capacity is zero, then there is no more flow to be sent
        if min_capacity == 0:
            break
        
        # Send the minimum capacity of flow from the source to the sink
        for v, c in graph[source]:
            if c == min_capacity:
                graph[source].remove((v, c))
                graph[v].remove((source, c))
                max_flow += min_capacity
                edges_used += 1
                break
    
    # Return the maximum flow and the number of edges used
    return max_flow, edges_used

