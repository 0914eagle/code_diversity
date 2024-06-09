
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery schedule with the first order
    schedule = [orders[0]]

    # Iterate through the remaining orders
    for order in orders[1:]:
        # Find the earliest time that the current order can be delivered
        earliest_time = order[0]
        for prev_order in schedule:
            earliest_time = max(earliest_time, prev_order[1] + graph[prev_order[2] - 1][order[2] - 1][1])

        # If the earliest time is after the current order's ready time, skip this order
        if earliest_time > order[1]:
            continue

        # Add the order to the schedule
        schedule.append(order)

    # Return the longest time a customer has to wait for delivery
    return max(order[0] - earliest_time for order in schedule)

