
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
    visited = [False] * (n + 1)
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue.extend(graph[vertex])
    
    # Find the maximum number of reachable vertices
    max_reachable = 0
    for i in range(1, n + 1):
        if visited[i]:
            max_reachable += 1
    
    # Find the minimum number of reachable vertices
    min_reachable = 0
    for i in range(1, n + 1):
        if visited[i]:
            min_reachable += 1
    
    # Create the plans
    plan1 = [max_reachable]
    plan2 = [min_reachable]
    for t, u, v in edges:
        if t == 1:
            plan1.append('+')
            plan2.append('+')
        else:
            if u == s:
                plan1.append('+')
                plan2.append('-')
            else:
                plan1.append('-')
                plan2.append('+')
    
    return plan1, plan2

