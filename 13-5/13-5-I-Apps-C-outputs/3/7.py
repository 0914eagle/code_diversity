
def get_max_flow(n, m, s, t, edges):
    # Initialize the graph with the given nodes and edges
    graph = {i: [] for i in range(n)}
    for u, v, c in edges:
        graph[u].append((v, c))
    
    # Initialize the residual graph with the given edges
    residual = {i: [] for i in range(n)}
    for u, v, c in edges:
        residual[u].append((v, c))
    
    # Initialize the flow to be 0
    flow = {i: 0 for i in range(n)}
    
    # Initialize the parent array to keep track of the BFS
    parent = [-1] * n
    
    # Find the maximum flow using the Edmonds-Karp algorithm
    while bfs(residual, s, t, parent):
        flow_through_edge = float('inf')
        u = t
        while u != s:
            v = parent[u]
            flow_through_edge = min(flow_through_edge, residual[v][parent[v]][1] - flow[v])
            u = v
        u = t
        while u != s:
            v = parent[u]
            residual[v][parent[v]][1] -= flow_through_edge
            residual[v][parent[v]][0] += flow_through_edge
            flow[v] += flow_through_edge
            u = v
    
    # Return the maximum flow and the edges used in the solution
    return flow[t], [(u, v, flow[v]) for u, v, c in edges if flow[v] > 0]

def bfs(graph, s, t, parent):
    # Initialize the queue with the source node
    queue = [s]
    
    # Initialize the visited array
    visited = [False] * len(graph)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        u = queue.pop(0)
        
        # If the node is the sink, return True
        if u == t:
            return True
        
        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if not visited[u]:
            visited[u] = True
            for v, c in graph[u]:
                if c > 0:
                    queue.append(v)
                    parent[v] = u
    
    # If the queue is empty and the sink has not been reached, return False
    return False

