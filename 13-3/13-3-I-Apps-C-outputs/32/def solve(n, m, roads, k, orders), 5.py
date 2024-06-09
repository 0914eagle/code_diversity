
def solve(n, m, roads, k, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Dijkstra's algorithm to find the shortest path from node 0 (pizzeria) to all other nodes
    dist = [float('inf')] * n
    dist[0] = 0
    visited = [False] * n

    for _ in range(n - 1):
        # Find the unvisited node with the minimum distance
        min_node = -1
        for i in range(n):
            if not visited[i] and (min_node == -1 or dist[i] < dist[min_node]):
                min_node = i

        # Mark the node as visited and update the distance of its neighbors
        visited[min_node] = True
        for neighbor, weight in graph[min_node]:
            if not visited[neighbor] and dist[min_node] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_node] + weight

    # Find the maximum delay for each order
    max_delay = 0
    for order in orders:
        s, u, t = order
        delay = dist[u - 1] + t - s
        max_delay = max(max_delay, delay)

    return max_delay

