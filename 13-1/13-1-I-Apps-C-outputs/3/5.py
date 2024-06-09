
def get_minimum_path_length(n, m, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].add(v)

    # Find all maximum length paths in the graph
    paths = []
    for i in range(1, n + 1):
        path = []
        visited = set()
        queue = [i]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                path.append(node)
                queue.extend(graph[node] - visited)
        paths.append(path)

    # Find the minimum length path that can be taken if at most one road is blocked
    min_length = float("inf")
    for path in paths:
        length = len(path)
        for i in range(1, n):
            if path[i] != path[i - 1] + 1:
                length -= 1
        min_length = min(min_length, length)

    return min_length

