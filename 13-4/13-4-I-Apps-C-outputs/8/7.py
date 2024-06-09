
def solve(N, R, flights, F, additional_flights):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph
    for a, b, c in flights:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Add additional flights to the graph
    for a, b, c in additional_flights:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path using Dijkstra's algorithm
    visited = [False] * (N + 1)
    queue = [(0, 1, [])]
    while queue:
        dist, node, path = heapq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        if node == N:
            return dist
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(queue, (dist + weight, neighbor, path + [neighbor]))
    return -1

