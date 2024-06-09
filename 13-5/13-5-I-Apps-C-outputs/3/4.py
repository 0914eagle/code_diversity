
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given nodes and edges
    graph = {i: set() for i in range(n)}
    for u, v, c in edges:
        graph[u].add((v, c))
        graph[v].add((u, c))
    
    # Initialize the source and sink nodes
    source = s
    sink = t
    
    # Initialize the flow and the number of edges used
    flow = 0
    edges_used = 0
    
    # While there is a path from the source to the sink
    while True:
        # Find a path from the source to the sink
        path = find_path(graph, source, sink)
        if not path:
            break
        
        # Find the minimum capacity of the path
        min_capacity = min(graph[u][v][1] for u, v in zip(path, path[1:]))
        
        # Add the minimum capacity to the flow
        flow += min_capacity
        
        # Update the graph with the new flow
        for u, v in zip(path, path[1:]):
            graph[u][v][1] -= min_capacity
            graph[v][u][1] += min_capacity
        
        # Increment the number of edges used
        edges_used += 1
    
    # Return the flow and the number of edges used
    return flow, edges_used

def find_path(graph, source, sink):
    # Initialize the queue with the source node
    queue = [source]
    
    # Initialize the visited nodes
    visited = set()
    
    # While the queue is not empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the current node is the sink, return the path
        if node == sink:
            path = [node]
            while node != source:
                path.append(node)
                node = prev[node]
            return path[::-1]
        
        # If the current node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            queue += [neighbor for neighbor, capacity in graph[node] if capacity > 0]
    
    # If no path is found, return an empty list
    return []

