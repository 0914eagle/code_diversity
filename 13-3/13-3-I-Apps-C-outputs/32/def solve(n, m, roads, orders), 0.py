
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their delivery time
    orders.sort(key=lambda x: x[2])

    # Initialize the delivery time for each order to 0
    delivery_times = [0] * len(orders)

    # Loop through the orders and calculate the delivery time for each order
    for i in range(len(orders)):
        order = orders[i]
        u, t = order[1] - 1, order[2]
        for j in range(i):
            prev_order = orders[j]
            if prev_order[1] - 1 == u:
                t = max(t, delivery_times[j] + graph[prev_order[1] - 1][prev_order[2] - 1][1])
        delivery_times[i] = t

    # Return the maximum delivery time
    return max(delivery_times)

