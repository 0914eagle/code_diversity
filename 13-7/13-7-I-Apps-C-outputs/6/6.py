
def get_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph based on the partnerships
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    dist, pred = dijkstra(graph, X, Y)

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path
    for i in range(len(pred) - 1):
        # Get the current and next bank in the path
        current_bank = pred[i]
        next_bank = pred[i + 1]

        # Check if the next bank is owned by SWERC
        if next_bank in SWERC_banks:
            # Get the fee for the transfer between the current and next bank
            fee = graph[current_bank][next_bank][1]

            # Update the largest fee if necessary
            largest_fee = max(largest_fee, fee)

    # Return the largest fee
    return largest_fee

def dijkstra(graph, start, end):
    # Initialize the distance and predecessor arrays
    dist = [float('inf')] * len(graph)
    pred = [None] * len(graph)

    # Set the distance of the start node to 0
    dist[start] = 0

    # Create a priority queue to hold the nodes to visit
    queue = [(0, start)]

    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        current_node = queue.pop(0)

        # Check if the current node is the end node
        if current_node[1] == end:
            # Return the distance and predecessor arrays
            return dist, pred

        # Relax the neighbors of the current node
        for neighbor, weight in graph[current_node[1]]:
            # Check if the neighbor has not been visited
            if dist[neighbor] == float('inf'):
                # Set the distance of the neighbor to the current distance + the weight
                dist[neighbor] = dist[current_node[1]] + weight

                # Set the predecessor of the neighbor to the current node
                pred[neighbor] = current_node[1]

                # Add the neighbor to the queue
                queue.append((dist[neighbor], neighbor))

    # Return the distance and predecessor arrays
    return dist, pred

