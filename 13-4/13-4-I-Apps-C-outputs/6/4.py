
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

    # Initialize a dictionary to store the cost of sending a crystal from city s to city t on each day
    costs = {}
    for s, t in queries:
        # Calculate the distance between city s and city t using the bitwise OR of all the road lengths
        distance = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if a in distances and b in distances[a]:
                    distance |= distances[a][b]

        # Add the cost for sending a crystal from city s to city t on this day
        costs[s, t] = distance

    return [costs[s, t] for s, t in queries]

