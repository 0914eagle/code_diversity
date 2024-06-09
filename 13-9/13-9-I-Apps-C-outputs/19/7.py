
def solve(n, m, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].add(v)

    # Find all possible paths of maximum length
    paths = []
    for i in range(1, n + 1):
        for j in graph[i]:
            paths.append([i, j])

    # Find the minimum length path that a winning racer would take if at most one of the roads is blocked off
    min_length = float("inf")
    for path in paths:
        length = len(path)
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if u != v and u in graph[v]:
                length -= 1
        min_length = min(min_length, length)

    return min_length

