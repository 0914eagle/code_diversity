
def solve(n, m, roads, q, queries):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for a, b, w in roads:
        if a not in distances:
            distances[a] = {}
        if b not in distances:
            distances[b] = {}
        distances[a][b] = w
        distances[b][a] = w

    # Fill in the distances for each city pair using the bitwise OR operation
    for city in distances:
        for other_city in distances[city]:
            if city != other_city:
                distances[city][other_city] = distances[city][other_city] | distances[other_city][city]

    # Calculate the cost of sending the crystal from s to t for each day
    costs = []
    for s, t in queries:
        cost = distances[s][t]
        costs.append(cost)

    return costs

