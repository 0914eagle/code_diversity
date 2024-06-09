
def get_largest_fee(n, p, x, y, partnerships, swerc_banks):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the transfer partnerships
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, x, y)

    # If there is no path between X and Y, return "Impossible"
    if dist[y] == float("inf"):
        return "Impossible"

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path and calculate the total fee
    for node in range(x, y + 1):
        if node in swerc_banks:
            largest_fee += dist[node]
        else:
            largest_fee += dist[node] + 1

    return largest_fee

def dijkstra(graph, src, dest):
    # Initialize the distance array with infinite values
    dist = [float("inf") for _ in range(len(graph))]

    # Initialize the previous array with -1
    prev = [-1 for _ in range(len(graph))]

    # Initialize a priority queue with the source node
    queue = [(0, src)]

    # Loop until the queue is empty
    while queue:
        # Get the minimum distance node from the queue
        node = heapq.heappop(queue)[1]

        # If the node is the destination, return the distance array and previous array
        if node == dest:
            return dist, prev

        # If the node is already processed, skip it
        if dist[node] != float("inf"):
            continue

        # Update the distance and previous array for the current node
        dist[node] = 0
        prev[node] = -1

        # Iterate through the node's neighbors
        for neighbor, weight in graph[node]:
            # If the neighbor is not processed, add it to the queue
            if dist[neighbor] == float("inf"):
                heapq.heappush(queue, (dist[node] + weight, neighbor))

    # Return the distance array and previous array
    return dist, prev

