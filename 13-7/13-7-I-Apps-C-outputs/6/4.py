
def get_largest_fee(num_banks, num_partnerships, bank_x, bank_y, partnerships, num_owned_banks, owned_banks):
    # Initialize a graph with the given number of banks
    graph = [[] for _ in range(num_banks + 1)]

    # Add edges to the graph based on the partnerships
    for i in range(num_partnerships):
        graph[partnerships[i][0]].append((partnerships[i][1], partnerships[i][2]))
        graph[partnerships[i][1]].append((partnerships[i][0], partnerships[i][2]))

    # Find the shortest path between bank X and bank Y using Dijkstra's algorithm
    dist, prev = dijkstra(graph, bank_x)

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path between bank X and bank Y
    for i in range(len(prev) - 1):
        # If the current bank is owned by SWERC, add the fee to the largest fee
        if prev[i] in owned_banks:
            largest_fee += graph[prev[i]][prev[i + 1]][1]

    return largest_fee

def dijkstra(graph, src):
    # Initialize the distance array and previous array with infinity
    dist = [float('inf')] * len(graph)
    prev = [None] * len(graph)

    # Set the distance of the source to 0 and its previous to itself
    dist[src] = 0
    prev[src] = src

    # Initialize a priority queue with the source
    q = [(0, src)]

    # Loop until the priority queue is empty
    while q:
        # Get the current node with the minimum distance
        u = heappop(q)

        # Loop through the neighbors of the current node
        for v, w in graph[u[1]]:
            # If the distance of the neighbor is greater than the current distance plus the weight of the edge, update the distance and previous arrays
            if dist[v] > dist[u[1]] + w:
                dist[v] = dist[u[1]] + w
                prev[v] = u[1]
                heappush(q, (dist[v], v))

    return dist, prev

