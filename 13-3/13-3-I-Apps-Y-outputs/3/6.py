
def solve(n, table):
    # Initialize the graph with the given table
    graph = {i: set() for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if table[i - 1][j - 1] != 0:
                graph[i].add(j)

    # Find the shortest path between each pair of villages
    distances = {(i, j): table[i - 1][j - 1] for i in range(1, n + 1) for j in range(1, n + 1) if i != j}
    paths = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                paths[(i, j)] = find_shortest_path(graph, distances, i, j)

    # Output the roads
    roads = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i, j) in paths:
                roads.append((i, j))
    return roads

def find_shortest_path(graph, distances, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == end:
                return path
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return []

