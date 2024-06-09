
def get_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct connections
    for x, y, cost in direct_connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Create a set to store the insecure buildings
    insecure_set = set(insecure_buildings)

    # Function to check if a path contains an insecure building
    def contains_insecure(path):
        return any(node in insecure_set for node in path)

    # Function to find the cheapest path between two nodes
    def find_cheapest_path(start, end):
        # Initialize a priority queue to store the nodes to visit
        queue = [(0, start, [start])]

        # Loop until the queue is empty
        while queue:
            # Get the node with the smallest cost from the queue
            cost, node, path = heapq.heappop(queue)

            # If the node is the end node, return the path
            if node == end:
                return path

            # If the node is insecure, skip it
            if node in insecure_set:
                continue

            # Add the neighbors of the node to the queue
            for neighbor, neighbor_cost in graph[node]:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor, path + [neighbor]))

        # If no path is found, return None
        return None

    # Function to find the cheapest network
    def find_cheapest_network():
        # Initialize the cost of the network to 0
        cost = 0

        # Loop through each insecure building
        for insecure_building in insecure_set:
            # Find the cheapest path from the insecure building to any other building
            path = find_cheapest_path(insecure_building, 0)

            # If no path is found, return None
            if path is None:
                return None

            # Add the cost of the path to the total cost of the network
            cost += sum(graph[node][1] for node in path)

        # Return the total cost of the network
        return cost

    # Find the cheapest network
    cost = find_cheapest_network()

    # If no network is found, return "impossible"
    if cost is None:
        return "impossible"

    # Otherwise, return the cost of the network
    return cost

