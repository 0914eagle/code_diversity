
def solve(n, m, roads, orders):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by the time they were placed
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery time for each order to 0
    delivery_time = [0] * len(orders)

    # Loop through the orders and calculate the delivery time for each order
    for i in range(len(orders)):
        order = orders[i]
        time = order[0]
        source = order[1] - 1
        destination = order[2] - 1

        # If this is the first order, set the delivery time to 0
        if i == 0:
            delivery_time[i] = 0
        else:
            # Find the previous order that was delivered
            previous_order = orders[i - 1]
            previous_time = previous_order[0]
            previous_destination = previous_order[2] - 1

            # Calculate the delivery time for this order
            delivery_time[i] = delivery_time[i - 1] + graph[previous_destination][previous_destination][1]

    # Return the longest delivery time
    return max(delivery_time)

