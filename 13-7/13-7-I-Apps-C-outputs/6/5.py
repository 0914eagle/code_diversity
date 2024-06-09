
def get_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph based on the partnerships
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, X, Y)

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path and calculate the total fee
    for node in range(X, Y + 1):
        # If the current node is a SWERC bank, add its fee to the total fee
        if node in SWERC_banks:
            largest_fee += graph[prev[node]][node - 1][1]

    return largest_fee

def dijkstra(graph, src, dest):
    # Initialize the distance and previous node arrays
    dist = [float('inf') for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]

    # Set the distance of the source node to 0 and its previous node to -1
    dist[src] = 0
    prev[src] = -1

    # Initialize a priority queue to store the nodes
    pq = [(0, src)]

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the smallest distance from the priority queue
        u = heappop(pq)[1]

        # If the node is the destination node, return the distance and previous node arrays
        if u == dest:
            return dist, prev

        # Relax the node
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heappush(pq, (dist[v], v))

    # If the destination node is not found, return -1
    return -1, -1

