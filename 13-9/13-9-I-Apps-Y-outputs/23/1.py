
def get_good_observatories(num_observatories, num_roads, elevations, roads):
    # Initialize a list to store the good observatories
    good_observatories = []
    
    # Iterate over each observatory
    for observatory in range(num_observatories):
        # Initialize a set to store the elevations of the observatories that can be reached from the current observatory using just one road
        reachable_elevations = set()
        
        # Iterate over each road
        for road in roads:
            # If the current observatory is the starting point of the road
            if road[0] == observatory:
                # Add the elevation of the ending point of the road to the set of reachable elevations
                reachable_elevations.add(elevations[road[1] - 1])
        
        # If the elevation of the current observatory is higher than all the reachable elevations
        if elevations[observatory] > max(reachable_elevations):
            # Add the current observatory to the list of good observatories
            good_observatories.append(observatory + 1)
    
    # Return the list of good observatories
    return good_observatories

