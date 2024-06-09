
def get_cheapest_network(n, m, p, insecure_buildings, direct_lines):
    # Initialize a graph with n buildings as nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct lines
    for x, y, cost in direct_lines:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Initialize the cost of the network to 0
    cost = 0

    # Iterate through each insecure building
    for building in insecure_buildings:
        # Find the shortest path to all other buildings from the current insecure building
        distances = dijkstra(graph, building - 1)

        # Add the cost of the shortest path to the total cost of the network
        cost += min(distances)

    return "impossible" if cost == float("inf") else cost

def dijkstra(graph, start):
    # Initialize the distances from the start node to all other nodes as infinity
    distances = [float("inf") for _ in range(len(graph))]
    distances[start] = 0

    # Initialize a priority queue with the start node and its distance from the start node
    queue = [(0, start)]

    # Loop until the priority queue is empty
    while queue:
        # Get the node with the minimum distance from the start node
        distance, node = heapq.heappop(queue)

        # If the node has already been visited, skip it
        if distance > distances[node]:
            continue

        # Update the distances of the node's neighbors
        for neighbor, cost in graph[node]:
            distance = distances[node] + cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

