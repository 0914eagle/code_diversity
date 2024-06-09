
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

    # Floyd-Warshall algorithm to calculate the shortest distance between all pairs of cities
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if i in distances and j in distances[i] and k in distances and k in distances[j]:
                    distances[i][j] = min(distances[i][j], distances[i][k] | distances[k][j])

    # Calculate the cost of sending the crystal from city s to city t for each day
    costs = []
    for s, t in queries:
        cost = distances[s][t]
        costs.append(cost)

    return costs

