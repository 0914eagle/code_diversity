
def solve(n, m, pairs):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for p, q, c in pairs:
        graph[p].append((q, c))
        graph[q].append((p, c))

    # Find the minimum spanning tree of the graph
    parent = [-1] * (n + 1)
    cost = [0] * (n + 1)
    priority_queue = [(0, 1)]
    while priority_queue:
        _, vertex = heapq.heappop(priority_queue)
        if parent[vertex] != -1:
            continue
        parent[vertex] = vertex
        for neighbor, weight in graph[vertex]:
            if parent[neighbor] == -1 and weight + cost[vertex] < cost[neighbor]:
                cost[neighbor] = weight + cost[vertex]
                heapq.heappush(priority_queue, (cost[neighbor], neighbor))

    # Check if the minimum spanning tree has n - 1 edges
    if len(priority_queue) != n - 1:
        return "impossible"

    # Calculate the total cost of the minimum spanning tree
    total_cost = 0
    for vertex in range(1, n + 1):
        if parent[vertex] != -1:
            total_cost += cost[vertex]

    return total_cost

