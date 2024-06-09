
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
        # Find the minimum cost path from the building to the tree
        path = dijkstra(graph, building - 1, tree)

        # Add the cost of the path to the total cost of the network
        total_cost += sum(cost for node, cost in path)

    return total_cost

def prim(graph, start):
    # Initialize the priority queue with the start node
    pq = [(0, start)]

    # Initialize the parent and key dictionaries
    parents = {start: None}
    keys = {start: 0}

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the minimum key from the priority queue
        node = heappop(pq)[1]

        # Iterate through the neighbors of the node
        for neighbor, cost in graph[node]:
            # If the neighbor is not in the priority queue, add it and set the parent and key
            if neighbor not in parents:
                parents[neighbor] = node
                keys[neighbor] = cost
                heappush(pq, (cost, neighbor))

            # If the neighbor is already in the priority queue and the cost is smaller, update the parent and key
            elif cost < keys[neighbor]:
                parents[neighbor] = node
                keys[neighbor] = cost
                heapify(pq)

    # Return the parent dictionary
    return parents

def dijkstra(graph, start, tree):
    # Initialize the priority queue with the start node
    pq = [(0, start)]

    # Initialize the distance dictionary
    distances = {start: 0}

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the minimum distance from the priority queue
        node = heappop(pq)[1]

        # If the node is not in the tree, add it to the tree and set the distance
        if node not in tree:
            tree[node] = distances[node]

        # Iterate through the neighbors of the node
        for neighbor, cost in graph[node]:
            # If the neighbor is not in the priority queue, add it and set the distance
            if neighbor not in distances:
                distances[neighbor] = distances[node] + cost
                heappush(pq, (distances[neighbor], neighbor))

            # If the neighbor is already in the priority queue and the distance is smaller, update the distance
            elif distances[neighbor] > distances[node] + cost:
                distances[neighbor] = distances[node] + cost
                heapify(pq)

    # Return the shortest path from the start node to the tree
    return reconstruct_path(start, tree)

def reconstruct_path(start, tree):
    # Initialize the path with the start node
    path = [start]

    # Initialize the current node with the start node
    current_node = start

    # Loop until the current node is not in the tree
    while current_node in tree:
        # Add the parent of the current node to the path
        path.append(tree[current_node])

        # Set the current node to its parent
        current_node = tree[current_node]

    # Return the path in reverse order
    return path[::-1]

