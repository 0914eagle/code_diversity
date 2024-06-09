
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given edges
    graph = [[] for _ in range(n)]
    for u, v, c in edges:
        graph[u].append((v, c))
    
    # Initialize the residual graph with the given edges
    residual_graph = [[] for _ in range(n)]
    for u, v, c in edges:
        residual_graph[u].append((v, c))
    
    # Initialize the maximum flow
    flow = 0
    
    # Initialize the parent array
    parent = [-1] * n
    
    # Initialize the visited array
    visited = [False] * n
    
    # Initialize the queue
    queue = []
    
    # Enqueue the source node
    queue.append(s)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        u = queue.pop(0)
        
        # If the node is the sink, break
        if u == t:
            break
        
        # Loop through the neighbors of the dequeued node
        for v, c in graph[u]:
            # If the neighbor is not visited, visit it
            if not visited[v]:
                # Enqueue the neighbor
                queue.append(v)
                
                # Mark the neighbor as visited
                visited[v] = True
                
                # Update the parent array
                parent[v] = u
    
    # If the sink is not visited, return -1
    if not visited[t]:
        return -1
    
    # Loop through the nodes in the graph
    for u in range(n):
        # Loop through the neighbors of the current node
        for v, c in graph[u]:
            # If the current node is the parent of the neighbor, and the flow is less than the capacity, update the flow
            if parent[u] == v and flow < c:
                flow = c
    
    # Initialize the maximum flow
    max_flow = 0
    
    # Initialize the current node
    current = t
    
    # Loop until the current node is the source
    while current != s:
        # Get the parent of the current node
        parent_node = parent[current]
        
        # Get the capacity of the edge from the parent to the current node
        capacity = graph[parent_node][current][1]
        
        # Update the maximum flow
        max_flow += min(flow, capacity)
        
        # Update the flow
        flow -= min(flow, capacity)
        
        # Update the current node
        current = parent_node
    
    # Return the maximum flow
    return max_flow

