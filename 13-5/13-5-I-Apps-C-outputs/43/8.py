
def shortest_paths(n, m, roads):
    # Initialize a dictionary to store the number of shortest paths for each road
    num_shortest_paths = {}
    
    # Loop through each road
    for road in roads:
        # Get the origin and destination cities and length of the road
        origin, destination, length = road
        
        # If the road is not already in the dictionary, add it with a count of 1
        if road not in num_shortest_paths:
            num_shortest_paths[road] = 1
        
        # Loop through all the other roads
        for other_road in roads:
            # If the other road is not the same as the current road
            if road != other_road:
                # Get the origin and destination cities and length of the other road
                other_origin, other_destination, other_length = other_road
                
                # If the destination city of the current road is the same as the origin city of the other road
                if destination == other_origin:
                    # Increment the count of shortest paths for the other road
                    num_shortest_paths[other_road] = num_shortest_paths.get(other_road, 0) + 1
    
    # Return the number of shortest paths for each road
    return [num_shortest_paths.get(road, 0) for road in roads]

