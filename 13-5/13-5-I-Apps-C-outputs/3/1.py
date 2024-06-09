
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given nodes and edges
    graph = {i: set() for i in range(n)}
    for u, v, c in edges:
        graph[u].add((v, c))
        graph[v].add((u, c))
    
    # Initialize the source and sink with infinite capacity
    source = {s: float('inf')}
    sink = {t: float('inf')}
    
    # Initialize the path and the flow
    path = {}
    flow = 0
    
    # While there is a path from the source to the sink
    while source:
        # Find a path from the source to the sink
        path = find_path(source, sink, graph)
        
        # If no path is found, break the loop
        if not path:
            break
        
        # Find the minimum capacity of the path
        min_capacity = float('inf')
        for u, v in path:
            min_capacity = min(min_capacity, graph[u][v][1] - graph[u][v][0])
        
        # Update the flow and the residual capacity of the edges in the path
        for u, v in path:
            graph[u][v][0] += min_capacity
            graph[v][u][0] -= min_capacity
            flow += min_capacity
        
        # Add the sink to the source if the sink is not already in the source
        if t not in source:
            source[t] = float('inf')
    
    # Return the flow and the number of edges in the path
    return flow, len(path)

def find_path(source, sink, graph):
    # Initialize the queue with the source node
    queue = [source]
    
    # Initialize the visited nodes
    visited = set()
    
    # While the queue is not empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the node is not in the visited nodes, mark it as visited and add it to the visited nodes
        if node not in visited:
            visited.add(node)
        
        # If the node is the sink, return the path
        if node == sink:
            path = []
            while node is not None:
                path.append(node)
                node = graph[node]
            return path[::-1]
        
        # Add the neighbors of the node to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # If no path is found, return an empty list
    return []

