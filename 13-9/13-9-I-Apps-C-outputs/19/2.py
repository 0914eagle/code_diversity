
def solve(n, m, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].add(v)

    # Find all maximum length paths in the graph
    max_paths = []
    for i in range(1, n + 1):
        path = []
        visited = set()
        queue = [i]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                path.append(node)
                queue += list(graph[node] - visited)
        max_paths.append(path)

    # Find the minimum length path that competitors can achieve if at most one of the roads is blocked off
    min_path_length = float("inf")
    for path in max_paths:
        blocked_road = path[0]
        for i in range(1, len(path)):
            if path[i] != blocked_road + 1:
                break
        min_path_length = min(min_path_length, len(path) - i)

    return min_path_length

