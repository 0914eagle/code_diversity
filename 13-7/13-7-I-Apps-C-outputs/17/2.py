
def solve(n, m, roads, orders):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their time of placement
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery schedule with the first order
    schedule = [orders[0]]

    # Iterate through the remaining orders
    for order in orders[1:]:
        # Find the earliest time that the delivery can be made for this order
        earliest_time = order[0]
        for prev_order in schedule:
            earliest_time = max(earliest_time, prev_order[1] + graph[prev_order[2] - 1][order[2] - 1][1])

        # Add the order to the schedule if it can be delivered before the current latest delivery time
        latest_delivery_time = schedule[-1][1]
        if earliest_time <= latest_delivery_time:
            schedule.append(order)

    # Return the longest time a customer has to wait for delivery
    return schedule[-1][1] - schedule[0][0]

