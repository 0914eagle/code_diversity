
def find_minimum_length_path(n, m, roads):
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
    
    # Find the minimum length path that a racer can take if at most one road is blocked
    min_length = float('inf')
    for path in max_paths:
        length = len(path)
        for i in range(n):
            for j in range(i+1, n):
                if (i, j) in roads or (j, i) in roads:
                    length -= 1
        min_length = min(min_length, length)
    
    return min_length

def dfs(graph, node, visited, path):
    if visited[node]:
        return
    visited[node] = True
    path.append(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited, path)

