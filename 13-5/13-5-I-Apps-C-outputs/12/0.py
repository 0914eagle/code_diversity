
def solve(a, b, n, m, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Janet's house
    distances = {1: 0}
    # Initialize a dictionary to store the previous intersection for each intersection
    previous = {1: None}
    
    # Loop through each intersection
    for i in range(1, n+1):
        # If the current intersection is not Janet's house,
        if i != n:
            # Loop through each road leading to the current intersection
            for road in roads:
                # If the road leads to the current intersection and the previous intersection is not None,
                if road[1] == i and previous[i] is not None:
                    # Update the shortest distance and previous intersection for the current intersection
                    distances[i] = min(distances[i], distances[previous[i]] + road[2])
                    previous[i] = previous[previous[i]]
    
    # Return the shortest distance from the starting intersection to Janet's house
    return distances[n]

