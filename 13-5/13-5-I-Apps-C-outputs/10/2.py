
def get_cheapest_network(n, m, p, insecure_buildings, potential_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the potential connections
    for connection in potential_connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    tree = prim(graph, 0)

    # Initialize the total cost of the network to 0
    total_cost = 0

    # Iterate through the insecure buildings and add their costs to the total cost
    for building in insecure_buildings:
        total_cost += graph[building - 1][0][1]

    # Return the total cost of the network if it is possible, otherwise return "impossible"
    return total_cost if total_cost <= m else "impossible"

# Prim's algorithm to find the minimum spanning tree of a graph
def prim(graph, start):
    # Initialize a priority queue with the start node and its cost as the key
    queue = [(0, start)]

    # Initialize a dictionary to keep track of the nodes that have been visited
    visited = {start: True}

    # Loop until the priority queue is empty
    while queue:
        # Get the node with the minimum cost from the priority queue
        cost, node = heapq.heappop(queue)

        # If the node has not been visited, mark it as visited and add its neighbors to the priority queue
        if node not in visited:
            visited[node] = True
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))

    # Return the minimum spanning tree
    return visited

