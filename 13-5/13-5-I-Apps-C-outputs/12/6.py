
def solve(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {1: 0}
    # Initialize a dictionary to store the previous intersection for each intersection
    previous = {1: None}
    # Loop through each road
    for u, v, t in roads:
        # If the destination intersection is not in the dictionary, add it
        if v not in distances:
            distances[v] = float('inf')
            previous[v] = u
        # If the distance through this road is less than the current shortest distance, update the shortest distance and previous intersection
        if distances[u] + t < distances[v]:
            distances[v] = distances[u] + t
            previous[v] = u
    
    # Loop through each intersection and find the shortest distance to Janet's house
    for i in range(2, n+1):
        if distances[i] < distances[1]:
            distances[1] = distances[i]
            previous[1] = i
    
    # Return the worst-case waiting time, which is the shortest distance from Richard's house to Janet's house plus the time it takes to travel from Janet's house to Richard's house
    return distances[1] + distances[n]

