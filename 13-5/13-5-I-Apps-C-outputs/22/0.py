
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b, l in roads:
        graph[a].add((b, l))
        graph[b].add((a, l))

    # Find the shortest path from the police car start to any exit
    import heapq
    queue = [(0, start_police, [])]
    visited = set()
    while queue:
        dist, curr, path = heapq.heappop(queue)
        if curr in visited:
            continue
        visited.add(curr)
        if curr in exits:
            return dist
        for neighbor, weight in graph[curr]:
            heapq.heappush(queue, (dist + weight, neighbor, path + [neighbor]))

    # If no path to any exit is found, return IMPOSSIBLE
    return "IMPOSSIBLE"

