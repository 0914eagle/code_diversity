
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
    
    # Find the minimum length path that can be taken if at most one road is blocked off
    min_length = float('inf')
    for path in paths:
        length = len(path)
        for i in range(n-1):
            u, v = path[i], path[i+1]
            if u != v and graph[u][v] == 1:
                length -= 1
        min_length = min(min_length, length)
    
    return min_length

def find_all_paths(graph, start, visited, path):
    path = path + [start]
    visited[start] = True
    if start == len(graph) - 1:
        return [path]
    paths = []
    for i in range(len(graph)):
        if not visited[i] and graph[start][i] == 1:
            paths += find_all_paths(graph, i, visited, path)
    return paths

