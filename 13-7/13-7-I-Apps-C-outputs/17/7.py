
def solve(n, m, roads, orders):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their arrival time
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery schedule with the pizza ready time
    schedule = [order[2] for order in orders]

    # Loop through the orders and update the delivery schedule
    for order in orders:
        u, _, t = order
        for v, d in graph[u - 1]:
            if schedule[v] > t + d:
                schedule[v] = t + d

    # Return the maximum waiting time
    return max(schedule)

