
def shortest_paths(n, m, roads):
    # Initialize a dictionary to store the number of shortest paths for each road
    num_shortest_paths = {}
    
    # Loop through each road
    for road in roads:
        # Get the origin and destination cities and the length of the road
        origin, destination, length = road
        
        # If this is the first road, initialize the number of shortest paths to 1
        if origin not in num_shortest_paths:
            num_shortest_paths[origin] = 1
        
        # If this is not the first road, add the number of shortest paths from the previous road
        else:
            num_shortest_paths[origin] += num_shortest_paths.get(destination, 0)
        
        # Add the number of shortest paths from this road to the destination city
        num_shortest_paths[destination] = num_shortest_paths.get(destination, 0) + 1
    
    # Return the number of shortest paths for each road
    return [num_shortest_paths.get(road, 0) for road in range(1, n + 1)]

