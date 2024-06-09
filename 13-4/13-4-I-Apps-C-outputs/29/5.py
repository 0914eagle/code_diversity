
def absurd_travel(n, m, railways):
    # Initialize a graph with the given railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)

    # Find the shortest path between the starting town (1) and the destination town (n)
    visited = set()
    queue = [(1, [], 0)]
    while queue:
        town, path, time = queue.pop(0)
        if town == n:
            return time
        if town in visited:
            continue
        visited.add(town)
        for neighbor in graph[town]:
            queue.append((neighbor, path + [neighbor], time + 1))

    # If no path exists, return -1
    return -1

