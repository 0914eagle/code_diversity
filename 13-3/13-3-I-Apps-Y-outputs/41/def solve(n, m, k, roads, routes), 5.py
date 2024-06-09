
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

    # Loop through each district
    for i in range(1, n + 1):
        # Loop through the neighbors of the current district
        for j, w in graph[i]:
            # If the distance from the current district to the neighboring district is less than the current minimum distance, update the minimum distance and the previous node
            if dist[i] + w < dist[j]:
                dist[j] = dist[i] + w
                prev[j] = i

    # Initialize the total cost of the courier routes as 0
    total_cost = 0

    # Loop through each courier route
    for a, b in routes:
        # If the previous node of the starting district is not -1, it means that there is a path from the starting district to the ending district
        if prev[a] != -1:
            # Add the cost of the path from the starting district to the ending district to the total cost
            total_cost += dist[b]
        # Otherwise, it means that there is no path from the starting district to the ending district, so the total cost is 0
        else:
            total_cost += 0

    return total_cost

