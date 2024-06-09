
def solve(n, m, k, roads, routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, w in roads:
        graph[x].add((y, w))
        graph[y].add((x, w))

    # Initialize the minimum distance from each district to itself as 0
    dist = {i: 0 for i in range(1, n + 1)}

    # Initialize the previous node for each district as -1
    prev = {i: -1 for i in range(1, n + 1)}

    # Loop through each district and find the minimum distance to each other district
    for i in range(1, n + 1):
        for j in graph[i]:
            if dist[i] + j[1] < dist[j[0]]:
                dist[j[0]] = dist[i] + j[1]
                prev[j[0]] = i

    # Find the minimum total cost of the courier routes
    total_cost = 0
    for a, b in routes:
        total_cost += dist[b]

    return total_cost

