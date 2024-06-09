
def shortest_paths(N, M, roads):
    # Initialize a dictionary to store the number of shortest paths for each road
    shortest_paths = {}
    
    # Loop through each road
    for road in roads:
        # Get the origin and destination cities and the length of the road
        origin, destination, length = road
        
        # If the road is not already in the dictionary, add it with a count of 1
        if road not in shortest_paths:
            shortest_paths[road] = 1
        
        # Loop through all the roads that have the same origin city as the current road
        for other_road in [r for r in roads if r[0] == origin]:
            # If the other road has the same destination city as the current road, increment the count for the current road
            if other_road[1] == destination:
                shortest_paths[road] += shortest_paths[other_road]
    
    # Return the number of shortest paths for each road
    return [shortest_paths[road] % 1000000007 for road in roads]

