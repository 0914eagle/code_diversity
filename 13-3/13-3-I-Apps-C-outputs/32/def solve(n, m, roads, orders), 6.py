
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their arrival time
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery time for each order to 0
    delivery_times = [0] * len(orders)

    # Loop through the orders and find the earliest delivery time for each order
    for i in range(len(orders)):
        current_time = orders[i][0]
        current_node = 0
        visited = set()
        queue = [(current_node, current_time)]

        while queue:
            node, time = queue.pop(0)
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, time + weight))
                    delivery_times[i] = max(delivery_times[i], time + weight)

    # Return the maximum delivery time
    return max(delivery_times)

