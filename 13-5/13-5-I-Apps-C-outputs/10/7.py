
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    tree = prim(graph, 0)

    # Initialize the total cost of the network to 0
    total_cost = 0

    # Iterate through the insecure buildings
    for building in insecure_buildings:
        # Find the shortest path from the building to the starting building (0)
        path = dijkstra(graph, building - 1)

        # Add the cost of the path to the total cost of the network
        total_cost += path[0]

    # Return the total cost of the network if it is possible, otherwise return "impossible"
    return total_cost if total_cost != float("inf") else "impossible"

# Prim's algorithm for finding the minimum spanning tree of a graph
def prim(graph, start):
    # Initialize the priority queue with the start node and its distance from the starting node
    queue = [(0, start)]

    # Initialize the parent array with -1 for all nodes
    parents = [-1] * len(graph)

    # Initialize the distance array with infinity for all nodes
    distances = [float("inf")] * len(graph)

    # Set the distance of the start node to 0
    distances[start] = 0

    # Loop until the priority queue is empty
    while queue:
        # Get the node with the minimum distance from the priority queue
        distance, node = heapq.heappop(queue)

        # If the node has already been visited, skip it
        if distances[node] < distance:
            continue

        # Update the parent array and the distance array
        parents[node] = distance
        distances[node] = distance

        # Add the node's neighbors to the priority queue
        for neighbor, cost in graph[node]:
            heapq.heappush(queue, (distance + cost, neighbor))

    # Return the parent array
    return parents

# Dijkstra's algorithm for finding the shortest path between two nodes in a graph
def dijkstra(graph, start):
    # Initialize the priority queue with the start node and its distance from the starting node
    queue = [(0, start)]

    # Initialize the distance array with infinity for all nodes
    distances = [float("inf")] * len(graph)

    # Set the distance of the start node to 0
    distances[start] = 0

    # Loop until the priority queue is empty
    while queue:
        # Get the node with the minimum distance from the priority queue
        distance, node = heapq.heappop(queue)

        # If the node has already been visited, skip it
        if distances[node] < distance:
            continue

        # Update the distance array
        distances[node] = distance

        # Add the node's neighbors to the priority queue
        for neighbor, cost in graph[node]:
            heapq.heappush(queue, (distance + cost, neighbor))

    # Return the distance array
    return distances

