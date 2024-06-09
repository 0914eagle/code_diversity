
def solve(n, m, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].add(v)
    
    # Find all possible paths of maximum length
    paths = []
    for u in range(1, n + 1):
        for v in graph[u]:
            path = [u, v]
            while v in graph and len(graph[v]) == 1:
                v = list(graph[v])[0]
                path.append(v)
            paths.append(path)
    
    # Find the minimum length path that competitors can achieve if at most one of the roads is blocked off
    min_length = float('inf')
    for path in paths:
        length = len(path)
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u].remove(v)
            graph[v].remove(u)
            if len(graph[u]) == 0:
                break
        else:
            min_length = min(min_length, length)
    
    return min_length

