
def get_longest_wait_time(orders, roads, pizzeria_location):
    # Initialize the longest wait time to 0
    longest_wait_time = 0

    # Create a graph representing the roads in Stockholm
    graph = {}
    for road in roads:
        graph[road[0]] = {road[1]: road[2]}

    # Sort the orders by their placement time
    sorted_orders = sorted(orders, key=lambda x: x[0])

    # Iterate through the orders and calculate the longest wait time
    for order in sorted_orders:
        # Get the time it takes to deliver the order
        delivery_time = get_delivery_time(graph, pizzeria_location, order[1], order[2])

        # Update the longest wait time if necessary
        if delivery_time > longest_wait_time:
            longest_wait_time = delivery_time

    return longest_wait_time

def get_delivery_time(graph, current_location, destination, order_time):
    # Initialize the delivery time to 0
    delivery_time = 0

    # Get the shortest path between the current location and the destination
    path = get_shortest_path(graph, current_location, destination)

    # Iterate through the path and calculate the delivery time
    for i in range(len(path) - 1):
        delivery_time += graph[path[i]][path[i + 1]]

    # Add the time it takes to deliver the order
    delivery_time += order_time

    return delivery_time

def get_shortest_path(graph, start, end):
    # Initialize the shortest path to the start node
    path = [start]

    # While the current node is not the end node, find the nearest neighbor
    current_node = start
    while current_node != end:
        # Get the neighbors of the current node
        neighbors = graph[current_node].keys()

        # Find the nearest neighbor
        nearest_neighbor = None
        min_distance = float('inf')
        for neighbor in neighbors:
            distance = graph[current_node][neighbor]
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = neighbor

        # Add the nearest neighbor to the path and set it as the current node
        path.append(nearest_neighbor)
        current_node = nearest_neighbor

    return path

# Test the function with example input
orders = [(1, 4, 2), (3, 3, 3), (4, 3, 6)]
roads = [(1, 2, 2), (2, 3, 4), (3, 4, 1), (4, 1, 2)]
pizzeria_location = 1
print(get_longest_wait_time(orders, roads, pizzeria_location))

