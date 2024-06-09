
def shortest_paths(n, m, roads):
    # Initialize a dictionary to store the number of shortest paths for each road
    shortest_paths = {}
    
    # Loop through each road
    for road in roads:
        # Get the origin and destination cities and the length of the road
        origin, destination, length = road
        
        # If the road is not already in the dictionary, add it with a count of 1
        if road not in shortest_paths:
            shortest_paths[road] = 1
        
        # Otherwise, increment the count by 1
        else:
            shortest_paths[road] += 1
    
    # Return the number of shortest paths for each road
    return [shortest_paths[road] for road in roads]

