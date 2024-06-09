
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
    reachable = [s]
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in reachable:
                reachable.append(neighbor)
                queue.append(neighbor)
    
    # Find the maximum number of reachable vertices by orienting undirected edges in both directions
    max_reachable = len(reachable)
    max_edges = []
    for u, v in edges:
        if u != s and v != s and (u, v) not in max_edges:
            max_edges.append((u, v))
            max_edges.append((v, u))
            reachable = [s]
            queue = [s]
            while queue:
                vertex = queue.pop(0)
                for neighbor in graph[vertex]:
                    if neighbor not in reachable:
                        reachable.append(neighbor)
                        queue.append(neighbor)
            if len(reachable) > max_reachable:
                max_reachable = len(reachable)
                max_edges = []
                for u, v in edges:
                    if u != s and v != s and (u, v) not in max_edges:
                        max_edges.append((u, v))
                        max_edges.append((v, u))
    
    # Find the minimum number of reachable vertices by orienting undirected edges in one direction
    min_reachable = len(reachable)
    min_edges = []
    for u, v in edges:
        if u != s and v != s and (u, v) not in min_edges:
            min_edges.append((u, v))
            reachable = [s]
            queue = [s]
            while queue:
                vertex = queue.pop(0)
                for neighbor in graph[vertex]:
                    if neighbor not in reachable:
                        reachable.append(neighbor)
                        queue.append(neighbor)
            if len(reachable) < min_reachable:
                min_reachable = len(reachable)
                min_edges = []
                for u, v in edges:
                    if u != s and v != s and (u, v) not in min_edges:
                        min_edges.append((u, v))
    
    return max_reachable, max_edges, min_reachable, min_edges

