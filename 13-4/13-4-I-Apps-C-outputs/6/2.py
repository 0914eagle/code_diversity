
def solve(n, m, roads, q, queries):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for a, b, w in roads:
        if a not in distances:
            distances[a] = {}
        distances[a][b] = w
    
    # Fill in the rest of the distances using the bitwise OR operation
    for a in distances:
        for b in distances[a]:
            for c in distances[a]:
                if b != c:
                    distances[a][c] = distances[a][b] | distances[b][c]
    
    # Calculate the cost of sending a crystal from city s to city t on each day
    costs = []
    for s, t in queries:
        costs.append(distances[s][t])
    
    return costs

