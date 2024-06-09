
def solve(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {1: 0}
    for i in range(2, n+1):
        distances[i] = float('inf')

    # Loop through each road
    for u, v, t in roads:
        # If the distance from the starting intersection to the ending intersection is shorter than the current shortest distance, update the distance
        if distances[u] + t < distances[v]:
            distances[v] = distances[u] + t

    # Return the maximum distance from any intersection to Janet's house
    return max(distances.values())

