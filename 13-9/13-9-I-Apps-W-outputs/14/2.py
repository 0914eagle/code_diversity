
def get_brain_latency(n, m, connectors):
    # Initialize a dictionary to store the distance between each pair of brains
    distances = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distances[(i, j)] = 0
            else:
                distances[(i, j)] = float('inf')

    # Fill in the distances between each pair of brains using the given connectors
    for connector in connectors:
        distances[(connector[0], connector[1])] = 1
        distances[(connector[1], connector[0])] = 1

    # Use Floyd-Warshall algorithm to find the shortest path between every pair of brains
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[(i, j)] = min(distances[(i, j)], distances[(i, k)] + distances[(k, j)])

    # Find the maximum distance between any two brains
    max_distance = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                max_distance = max(max_distance, distances[(i, j)])

    return max_distance

