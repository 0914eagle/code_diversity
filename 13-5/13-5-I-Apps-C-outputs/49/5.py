
def get_min_path_length(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u - 1].append(v - 1)
    
    # Find all maximum length paths in the graph
    max_paths = []
    for i in range(n):
        visited = [False] * n
        max_paths.extend(dfs(graph, i, visited))
    
    # Find the minimum length path that can be taken if at most one road is blocked
    min_path_length = float('inf')
    for path in max_paths:
        path_length = len(path)
        for i in range(n):
            for j in range(i + 1, n):
                if [path[i], path[j]] in roads:
                    path_length -= 1
        min_path_length = min(min_path_length, path_length)
    
    return min_path_length

def dfs(graph, start, visited):
    visited[start] = True
    paths = []
    for neighbor in graph[start]:
        if not visited[neighbor]:
            paths.extend(dfs(graph, neighbor, visited))
    if not paths:
        paths.append([start])
    return paths

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append([u, v])
    print(get_min_path_length(n, m, roads))

