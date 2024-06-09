
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the roads
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their delivery time
    orders.sort(key=lambda x: x[2])

    # Initialize the delivery schedule with the first order
    schedule = [orders[0]]

    # Iterate through the remaining orders
    for order in orders[1:]:
        # Find the earliest time that the current order can be delivered
        earliest_time = order[2]
        for prev_order in schedule:
            earliest_time = max(earliest_time, prev_order[2] + graph[prev_order[1] - 1][order[1] - 1][1])

        # Add the current order to the schedule if it can be delivered by the earliest time
        if earliest_time <= order[2]:
            schedule.append(order)

    # Return the longest waiting time for any customer
    return max(order[2] - order[1] for order in schedule)

