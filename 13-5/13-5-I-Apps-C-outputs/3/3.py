
def solve_problem(n, m, s, t, edges):
    # Initialize variables
    flow_graph = {}
    flow_graph[s] = {}
    flow_graph[t] = {}
    for edge in edges:
        u, v, c = edge
        flow_graph[u] = flow_graph.get(u, {})
        flow_graph[u][v] = c
        flow_graph[v] = flow_graph.get(v, {})
        flow_graph[v][u] = 0
    
    # Find maximum flow using Ford-Fulkerson algorithm
    max_flow = 0
    while True:
        # Find augmenting path using BFS
        queue = [s]
        visited = set()
        parent = {}
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                if node == t:
                    break
                for neighbor, capacity in flow_graph[node].items():
                    if capacity > 0 and neighbor not in visited:
                        parent[neighbor] = node
                        queue.append(neighbor)
        
        # If there is no augmenting path, stop
        if t not in visited:
            break
        
        # Find minimum capacity of augmenting path
        path_flow = float('inf')
        node = t
        while node != s:
            path_flow = min(path_flow, flow_graph[parent[node]][node])
            node = parent[node]
        
        # Update flow
        node = t
        while node != s:
            flow_graph[parent[node]][node] -= path_flow
            flow_graph[node][parent[node]] += path_flow
            node = parent[node]
        
        # Update maximum flow
        max_flow += path_flow
    
    # Find edges with positive flow
    edges_with_flow = []
    for u, v, c in edges:
        if flow_graph[u][v] > 0:
            edges_with_flow.append((u, v, flow_graph[u][v]))
    
    # Return result
    return n, max_flow, len(edges_with_flow), edges_with_flow

