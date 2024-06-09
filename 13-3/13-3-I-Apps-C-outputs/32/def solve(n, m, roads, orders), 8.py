
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their time of placement
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
            # Find the previous order that was placed before this order
            previous_order = orders[i - 1]
            previous_time = previous_order[0]
            previous_destination = previous_order[2] - 1

            # Calculate the delivery time for this order by finding the shortest path between the previous order's destination and this order's source
            delivery_time[i] = delivery_time[i - 1] + shortest_path(graph, previous_destination, source)

    # Return the maximum delivery time among all orders
    return max(delivery_time)

def shortest_path(graph, source, destination):
    # Initialize a queue and enqueue the source node
    queue = [source]

    # Initialize a visited array and mark the source node as visited
    visited = [False] * len(graph)
    visited[source] = True

    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # If the node is the destination, return the delivery time
        if node == destination:
            return visited[node]

        # Enqueue the neighboring nodes that have not been visited
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = visited[node] + weight

    # If the destination is not found, return -1
    return -1

