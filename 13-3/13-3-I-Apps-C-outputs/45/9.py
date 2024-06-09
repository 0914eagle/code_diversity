
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    # Find all reachable vertices from vertex s
    reachable = set([s])
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    
    # Find the maximum number of reachable vertices by orienting all undirected edges in one direction
    max_reachable = len(reachable)
    max_edges = []
    for t, u, v in edges:
        if t == 2 and u != v:
            max_edges.append((u, v))
    
    # Find the minimum number of reachable vertices by orienting all undirected edges in the opposite direction
    min_reachable = 0
    min_edges = []
    for t, u, v in edges:
        if t == 2 and u != v:
            min_edges.append((v, u))
    
    return max_reachable, max_edges, min_reachable, min_edges

