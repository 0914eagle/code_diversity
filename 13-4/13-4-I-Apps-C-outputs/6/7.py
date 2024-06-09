
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
    for a in distances:
        for b in distances[a]:
            for c in distances[a]:
                if c != b:
                    distances[a][b] |= distances[a][c]

    # Calculate the cost for each query
    costs = []
    for s, t in queries:
        costs.append(distances[s][t])

    return costs

