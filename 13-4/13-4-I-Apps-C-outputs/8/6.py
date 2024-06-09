
def solve(N, R, flights, F, additional_flights):
    # Initialize a graph with the given number of nodes (airports)
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph based on the given flights
    for a, b, c in flights:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Add edges to the graph based on the additional flights
    for a, b, c in additional_flights:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Use a priority queue to keep track of the next flight to visit
    queue = [(0, 1, set())]
    visited = set()

    # Loop until all reviews have been made
    while len(visited) < R:
        # Get the next flight to visit from the priority queue
        cost, node, visited_nodes = heapq.heappop(queue)

        # If the current node is a review, mark it as visited and continue
        if node in visited_nodes:
            continue

        # Add the current node to the visited set
        visited.add(node)

        # Add the cost of the current flight to the total cost
        total_cost += cost

        # Add the neighbors of the current node to the priority queue
        for neighbor, weight in graph[node]:
            if neighbor not in visited_nodes:
                heapq.heappush(queue, (weight, neighbor, visited_nodes | {node}))

    # Return the total cost of the flights
    return total_cost

