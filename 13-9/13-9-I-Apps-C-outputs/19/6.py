
def solve(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append(v-1)
    
    # Find all maximum length paths in the graph
    max_paths = []
    for i in range(n):
        path = []
        visited = [False] * n
        dfs(graph, i, visited, path)
        max_paths.append(path)
    
    # Find the minimum length path that can be taken if at most one road is blocked off
    min_length = float('inf')
    for path in max_paths:
        length = len(path)
        for i in range(n-1):
            u, v = path[i], path[i+1]
            if u != v and [u, v] not in roads:
                length -= 1
        min_length = min(min_length, length)
    
    return min_length

def dfs(graph, start, visited, path):
    visited[start] = True
    path.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, path)
    return path

