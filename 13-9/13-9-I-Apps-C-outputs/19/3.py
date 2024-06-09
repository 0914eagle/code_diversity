
def solve(n, m, roads):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].add(v)

    # Find all possible paths from station 1 to station n
    paths = []
    for path in all_paths(graph, 1, n):
        paths.append(path)

    # Find the path with the maximum length
    max_length = 0
    for path in paths:
        length = len(path) - 1
        if length > max_length:
            max_length = length

    # Return the minimum length path that a winner can take if at most one road is blocked
    return max_length

def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(all_paths(graph, node, end, path))
    return paths

