
def solve(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[n] = 0

    # Loop through each road
    for u, v, t in roads:
        # If the current distance from intersection u to Janet's house is less than the current distance from intersection v to Janet's house, update the distance from intersection v to Janet's house
        if distances[u] + t < distances[v]:
            distances[v] = distances[u] + t

    # Return the maximum waiting time, which is the maximum distance from any intersection to Janet's house minus the minimum distance from any intersection to Janet's house
    return max(distances.values()) - min(distances.values())

