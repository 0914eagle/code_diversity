
def solve(n, table):
    # Initialize the graph with the given table
    graph = {i: set() for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if table[i - 1][j - 1] != 0:
                graph[i].add(j)

    # Find the shortest path between each pair of villages
    distances = {(i, j): table[i - 1][j - 1] for i in range(1, n + 1) for j in range(1, n + 1) if i != j}
    paths = {(i, j): [] for i in range(1, n + 1) for j in range(1, n + 1) if i != j}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                path, dist = find_shortest_path(graph, distances, i, j)
                paths[(i, j)] = path
                distances[(i, j)] = dist

    # Construct the output
    output = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and distances[(i, j)] != 0:
                output.append([i, j])

    return output

def find_shortest_path(graph, distances, start, end):
    visited = set()
    queue = [(start, [start], 0)]
    while queue:
        (node, path, dist) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return path, dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], dist + distances[(node, neighbor)]))
    return [], 0

