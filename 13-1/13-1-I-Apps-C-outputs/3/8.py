
def solve(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append(v-1)
    
    # Find all maximum length paths in the graph
    paths = []
    for i in range(n):
        visited = [False] * n
        paths += find_all_paths(graph, i, visited, [])
    
    # Find the minimum length path that a racer can take if at most one road is blocked off
    min_length = float('inf')
    for path in paths:
        length = len(path)
        for i in range(n):
            for j in range(i+1, n):
                if [path[i], path[j]] in roads:
                    length -= 1
        min_length = min(min_length, length)
    
    return min_length

def find_all_paths(graph, start, visited, path):
    path = path + [start]
    visited[start] = True
    if start == len(graph) - 1:
        return [path]
    paths = []
    for node in graph[start]:
        if not visited[node]:
            paths += find_all_paths(graph, node, visited, path)
    return paths

