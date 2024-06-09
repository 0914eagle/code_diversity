
def get_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph based on the transfer partnerships
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, X, Y)

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path and calculate the total fee
    for i in range(len(prev) - 1):
        bank_a = prev[i]
        bank_b = prev[i + 1]
        fee = graph[bank_a][bank_b][1]
        largest_fee += fee

    # Add the fee for the final transfer between X and Y
    largest_fee += graph[Y][X][1]

    # Check if the largest fee is greater than or equal to the minimum fee required by the government
    if largest_fee >= M:
        return largest_fee
    else:
        return "Impossible"

def dijkstra(graph, src, dest):
    # Initialize the distance and previous node arrays
    dist = [float("inf") for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]

    # Set the distance of the source node to 0 and its previous node to -1
    dist[src] = 0
    prev[src] = -1

    # Initialize a priority queue to store the nodes to be processed
    queue = [(0, src)]

    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        curr_dist, curr_node = heapq.heappop(queue)

        # If the current node is the destination node, return the distance and previous node arrays
        if curr_node == dest:
            return dist, prev

        # If the current node has not been processed, process it
        if curr_dist < dist[curr_node]:
            for neighbor, weight in graph[curr_node]:
                # If the neighbor has not been processed, add it to the queue
                if dist[neighbor] == float("inf"):
                    heapq.heappush(queue, (curr_dist + weight, neighbor))

                    # Update the distance and previous node arrays
                    dist[neighbor] = curr_dist + weight
                    prev[neighbor] = curr_node

    # If the destination node has not been reached, return -1
    return -1

