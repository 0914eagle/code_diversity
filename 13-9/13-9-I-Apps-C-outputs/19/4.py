
def find_min_path_length(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append(v-1)

    # Find all maximum length paths in the graph
    max_length_paths = []
    for i in range(n):
        visited = [False] * n
        max_length_paths.extend(find_max_length_paths(graph, i, visited))

    # Find the minimum length path that competitors can achieve if at most one of the roads is blocked off
    min_length = float('inf')
    for path in max_length_paths:
        length = len(path)
        for i in range(n):
            for j in range(i+1, n):
                if [i+1, j+1] in roads:
                    length -= 1
        min_length = min(min_length, length)

    return min_length

def find_max_length_paths(graph, start, visited):
    visited[start] = True
    paths = []
    for neighbor in graph[start]:
        if not visited[neighbor]:
            paths.extend(find_max_length_paths(graph, neighbor, visited))
    if not paths:
        paths.append([start])
    for path in paths:
        path.append(start)
    return paths

