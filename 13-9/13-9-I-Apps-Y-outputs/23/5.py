
def get_good_observatories(elevations, roads):
    # Initialize a set to store the good observatories
    good_observatories = set()

    # Loop through each observatory and its elevation
    for observatory, elevation in enumerate(elevations):
        # Check if the observatory is already in the good observatories set
        if observatory in good_observatories:
            continue

        # Loop through each road and its endpoints
        for road in roads:
            # Check if the observatory is the starting point of the road
            if road[0] == observatory:
                # Add the ending point of the road to the good observatories set
                good_observatories.add(road[1])

        # Check if the elevation of the observatory is higher than that of all its reachable observatories
        if elevation > max(elevations[obs] for obs in good_observatories):
            # Add the observatory to the good observatories set
            good_observatories.add(observatory)

    # Return the number of good observatories
    return len(good_observatories)

