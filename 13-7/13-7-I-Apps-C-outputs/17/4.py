
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their departure time
    orders.sort(key=lambda x: x[1])

    # Initialize the delivery schedule with the first order
    schedule = [(orders[0][1], orders[0][0])]

    # Loop through the remaining orders
    for order in orders[1:]:
        # Find the earliest possible departure time for the current order
        earliest_departure = schedule[-1][0] + graph[schedule[-1][1]][order[0] - 1][1]

        # If the earliest possible departure time is later than the current order's arrival time,
        # add the order to the schedule and continue to the next order
        if earliest_departure >= order[1]:
            schedule.append((order[1], order[0]))
            continue

        # If the earliest possible departure time is earlier than the current order's arrival time,
        # find the latest possible departure time for the current order
        latest_departure = schedule[-1][0] + graph[schedule[-1][1]][order[0] - 1][1]

        # Loop through the schedule and find the earliest departure time that is later than the current order's arrival time
        for i in range(len(schedule) - 1, -1, -1):
            if schedule[i][0] + graph[schedule[i][1]][order[0] - 1][1] >= order[1]:
                latest_departure = schedule[i][0] + graph[schedule[i][1]][order[0] - 1][1]
                break

        # Add the order to the schedule with the latest possible departure time
        schedule.append((latest_departure, order[0]))

    # Return the maximum waiting time for any customer
    return max(order[1] - schedule[i][0] for i, order in enumerate(orders))

