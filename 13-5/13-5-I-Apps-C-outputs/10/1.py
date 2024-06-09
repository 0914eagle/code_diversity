
def get_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct connections
    for x, y, cost in direct_connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the shortest path between all pairs of nodes using Dijkstra's algorithm
    distances = dijkstra(graph, 0)

    # Initialize the total cost of the network to 0
    total_cost = 0

    # Iterate over each insecure building
    for building in insecure_buildings:
        # Find the shortest path from the first building to the current insecure building
        path = dijkstra(graph, 0)[building - 1]

        # Add the cost of the path to the total cost of the network
        total_cost += path[1]

    # Return the total cost of the network if it is possible, otherwise return "impossible"
    return "impossible" if total_cost == float("inf") else total_cost

# Dijkstra's algorithm for finding the shortest path between all pairs of nodes in a graph
def dijkstra(graph, source):
    # Initialize the distances from the source node to all other nodes as infinity
    distances = [float("inf") for _ in range(len(graph))]
    distances[source] = 0

    # Initialize a priority queue with the source node and its distance from the source
    queue = [(0, source)]

    # Loop until the priority queue is empty
    while queue:
        # Get the node with the minimum distance from the source
        node, dist = heapq.heappop(queue)

        # If the distance of the node is less than the current minimum distance, skip it
        if distances[node] < dist:
            continue

        # Iterate over the neighbors of the node
        for neighbor, cost in graph[node]:
            # If the distance of the neighbor is greater than the distance of the node plus the cost of the edge, update the distance of the neighbor
            if distances[neighbor] > dist + cost:
                distances[neighbor] = dist + cost
                heapq.heappush(queue, (distances[neighbor], neighbor))

    return distances

