
def get_largest_fee(N, P, X, Y, M, banks, partnerships):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph based on the partnerships
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, X, Y)

    # If there is no path between X and Y, return "Impossible"
    if dist[Y] == float("inf"):
        return "Impossible"

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the path between X and Y
    for i in range(X, Y):
        # If the current node is not a bank owned by SWERC, continue
        if i not in banks:
            continue

        # Find the next node in the path that is a bank owned by SWERC
        next_node = prev[i]

        # If there is no next node, break
        if next_node == -1:
            break

        # Find the fee for the edge between the current node and the next node
        fee = graph[i][next_node][1]

        # Update the largest fee if necessary
        largest_fee = max(largest_fee, fee)

    # Return the largest fee
    return largest_fee

def dijkstra(graph, src, dest):
    # Initialize the distance and previous node arrays
    dist = [float("inf") for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]

    # Set the distance of the source node to 0
    dist[src] = 0

    # Create a min heap to store the nodes
    heap = [(0, src)]

    # Loop until the heap is empty
    while heap:
        # Get the minimum distance and node from the heap
        d, u = heapq.heappop(heap)

        # If the distance is already smaller than the current distance, continue
        if dist[u] < d:
            continue

        # Iterate through the neighbors of the current node
        for v, w in graph[u]:
            # If the distance to the neighbor is smaller than the current distance, update the distance and previous node
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u

                # Push the neighbor into the heap
                heapq.heappush(heap, (dist[v], v))

    # Return the distance and previous node arrays
    return dist, prev

