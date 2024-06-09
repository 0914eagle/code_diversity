
def solve(n, m, roads, k, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the roads
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their delivery time
    orders.sort(key=lambda x: x[2])

    # Initialize the delivery time for each order to 0
    delivery_times = [0] * k

    # Loop through the orders and calculate the delivery time for each order
    for i in range(k):
        order = orders[i]
        u, t = order[1], order[2]
        delivery_times[i] = t
        for neighbor, weight in graph[u - 1]:
            if delivery_times[neighbor] == 0:
                delivery_times[neighbor] = t + weight

    # Return the maximum delivery time
    return max(delivery_times)

