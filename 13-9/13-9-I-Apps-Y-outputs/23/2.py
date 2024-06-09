
def get_good_observatories(n, m, heights, roads):
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    # Iterate over each observatory
    for observatory in range(n):
        # Initialize a set to store the elevations of the observatories that can be reached from the current observatory
        reachable_elevations = set()
        
        # Iterate over each road
        for road in roads:
            # If the current observatory is one of the endpoints of the road
            if observatory in road:
                # Add the other endpoint of the road to the set of reachable observatories
                reachable_elevations.add(heights[road[0] if road[1] != observatory else road[1]])
        
        # If the elevation of the current observatory is higher than all the elevations of the reachable observatories
        if heights[observatory] > max(reachable_elevations):
            # Add the current observatory to the set of good observatories
            good_observatories.add(observatory)
    
    # Return the number of good observatories
    return len(good_observatories)

