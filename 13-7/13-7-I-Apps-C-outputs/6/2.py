
def get_largest_fee(N, P, X, Y, M, banks, transfer_partnerships):
    # Initialize a graph with all banks as nodes
    graph = [[] for _ in range(N + 1)]

    # Add edges between banks based on transfer partnerships
    for a, b, c in transfer_partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Find the shortest path between X and Y using Dijkstra's algorithm
    visited = [False] * (N + 1)
    queue = [(0, X)]
    while queue:
        dist, node = heapq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        if node == Y:
            break
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(queue, (dist + weight, neighbor))

    # If there is no path between X and Y, return "Impossible"
    if not visited[Y]:
        return "Impossible"

    # If the fee on each transfer can be infinitely large, return "Infinity"
    if M == N:
        return "Infinity"

    # Initialize the largest fee to 0
    largest_fee = 0

    # Iterate through the shortest path between X and Y
    for node in range(X, Y + 1):
        # If the current node is not a bank owned by SWERC, skip it
        if node not in banks:
            continue
        # If the current node is the destination bank, break the loop
        if node == Y:
            break
        # Find the next node in the shortest path that is a bank owned by SWERC
        for neighbor, weight in graph[node]:
            if neighbor in banks and neighbor > node:
                largest_fee += weight
                break

    return largest_fee

