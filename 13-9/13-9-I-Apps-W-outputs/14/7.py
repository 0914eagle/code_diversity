
def zombie_latency(brains, connectors):
    # Initialize a dictionary to store the distance between each pair of brains
    distance = {}
    for i in range(1, len(brains) + 1):
        for j in range(i, len(brains) + 1):
            distance[(i, j)] = 0

    # Fill in the dictionary with the distances between each pair of brains
    for connector in connectors:
        distance[tuple(sorted(connector))] = 1

    # Find the maximum distance between any two brains
    max_distance = 0
    for i in range(1, len(brains) + 1):
        for j in range(i, len(brains) + 1):
            if distance[(i, j)] > max_distance:
                max_distance = distance[(i, j)]

    return max_distance

