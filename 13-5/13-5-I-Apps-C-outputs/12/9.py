
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
    
    # Loop through each intersection
    for i in range(2, n+1):
        # If the intersection is not in the dictionary, add it
        if i not in distances:
            distances[i] = float('inf')
            previous[i] = None
        # If the distance through this road is less than the current shortest distance, update the shortest distance and previous intersection
        for u, v, t in roads:
            if i == u and distances[u] + t < distances[v]:
                distances[v] = distances[u] + t
                previous[v] = u
    
    # Find the shortest distance from the starting intersection to Janet's house
    shortest_distance = float('inf')
    for i in range(1, n+1):
        if distances[i] < shortest_distance:
            shortest_distance = distances[i]
    
    # Find the worst case waiting time
    worst_case = shortest_distance + b
    
    return worst_case

