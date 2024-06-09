
def solve(n, x, edges):
    # Create a graph from the edges
    graph = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the shortest path from the root to the target vertex
    visited = set()
    queue = [(1, [1])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == x:
            return len(path) - 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    # If the target vertex is not reachable, return -1
    return -1

