
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
        # If the shortest distance to the destination intersection is greater than the distance through this road, update the shortest distance and the previous intersection
        if distances[v] > distances[u] + t:
            distances[v] = distances[u] + t
            previous[v] = u
    
    # Find the shortest distance from Richard's house to Janet's house
    shortest_distance = min(distances.values())
    # Initialize a variable to store the worst case waiting time
    worst_case = float('inf')
    # Loop through each possible time that Janet could be ready
    for t in range(a, b + 1):
        # If the shortest distance to Janet's house is less than or equal to the time it takes to travel to the nearest intersection, the worst case waiting time is 0
        if shortest_distance <= t:
            worst_case = 0
            break
        # If the shortest distance to Janet's house is greater than the time it takes to travel to the nearest intersection, the worst case waiting time is the time it takes to travel to the nearest intersection
        else:
            worst_case = t - shortest_distance
    
    return worst_case

