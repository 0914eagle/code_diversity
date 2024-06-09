
def get_largest_fee(num_banks, num_partnerships, bank_x, bank_y, partnerships, num_swerc_banks, swerc_banks):
    # Initialize a graph with the given banks
    graph = [[] for _ in range(num_banks + 1)]

    # Add edges between partners
    for i in range(num_partnerships):
        graph[partnerships[i][0]].append((partnerships[i][1], partnerships[i][2]))
        graph[partnerships[i][1]].append((partnerships[i][0], partnerships[i][2]))

    # Find the shortest path between bank X and bank Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, bank_x)

    # Initialize the largest fee to 0
    largest_fee = 0

    # Loop through the shortest path and calculate the total fee
    for i in range(len(prev) - 1):
        largest_fee += graph[prev[i]][prev[i + 1]][1]

    # If the largest fee is greater than or equal to the number of SWERC banks, return Infinity
    if largest_fee >= num_swerc_banks:
        return "Infinity"

    # Otherwise, return the largest fee
    return largest_fee

# Dijkstra's algorithm
def dijkstra(graph, start):
    # Initialize the distance and previous node for each node
    dist = [float("inf") for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]

    # Set the distance for the starting node to 0
    dist[start] = 0

    # Loop until all nodes have been visited
    for i in range(len(graph)):
        # Find the unvisited node with the smallest distance
        min_node = None
        for j in range(len(graph)):
            if dist[j] < dist[min_node] and dist[j] != float("inf"):
                min_node = j

        # If there are no unvisited nodes, return the distances and previous nodes
        if min_node is None:
            return dist, prev

        # Visit the node
        for neighbor in graph[min_node]:
            new_dist = dist[min_node] + neighbor[1]
            if new_dist < dist[neighbor[0]]:
                dist[neighbor[0]] = new_dist
                prev[neighbor[0]] = min_node

    # Return the distances and previous nodes
    return dist, prev

