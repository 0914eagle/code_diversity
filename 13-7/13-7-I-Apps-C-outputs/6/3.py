
def solve(N, P, X, Y, M, banks, fees):
    # Initialize the graph with the given transfer partnerships
    graph = [[] for _ in range(N + 1)]
    for i in range(P):
        graph[fees[i][0]].append((fees[i][1], fees[i][2]))
        graph[fees[i][1]].append((fees[i][0], fees[i][2]))
    
    # Initialize the minimum distance from X to Y as infinity
    dist = [float('inf')] * (N + 1)
    dist[X] = 0
    
    # Initialize the previous node for each node as -1
    prev = [-1] * (N + 1)
    
    # Loop through all nodes in the graph
    for node in range(1, N + 1):
        # Loop through all neighbors of the current node
        for neighbor, cost in graph[node]:
            # If the distance to the neighbor through the current node is less than the current minimum distance, update the minimum distance and the previous node
            if dist[node] + cost < dist[neighbor]:
                dist[neighbor] = dist[node] + cost
                prev[neighbor] = node
    
    # If the minimum distance to Y is infinity, return "Impossible"
    if dist[Y] == float('inf'):
        return "Impossible"
    
    # Initialize the maximum fee as 0
    max_fee = 0
    
    # Loop through all nodes in the path from X to Y
    node = Y
    while node != X:
        # If the previous node is not -1, add the fee to the maximum fee
        if prev[node] != -1:
            max_fee += graph[prev[node]][node][1]
        # Set the node as the previous node
        node = prev[node]
    
    # Return the maximum fee
    return max_fee

