
def get_good_observatories(num_observatories, num_roads, observatory_elevations, roads):
    # Initialize a list to store the good observatories
    good_observatories = []

    # Iterate over each observatory
    for observatory in range(num_observatories):
        # Check if the observatory is good
        if is_good_observatory(observatory, observatory_elevations, roads):
            # If it is good, add it to the list of good observatories
            good_observatories.append(observatory)

    # Return the list of good observatories
    return good_observatories

def is_good_observatory(observatory, observatory_elevations, roads):
    # Get the elevation of the current observatory
    current_elevation = observatory_elevations[observatory]

    # Iterate over each road
    for road in roads:
        # Check if the current observatory is connected to the other observatory in the road
        if road[0] == observatory or road[1] == observatory:
            # If it is connected, get the elevation of the other observatory
            other_observatory = road[0] if road[1] != observatory else road[1]
            other_elevation = observatory_elevations[other_observatory]

            # Check if the elevation of the current observatory is higher than that of the other observatory
            if current_elevation <= other_elevation:
                # If it is not, the current observatory is not good
                return False

    # If the current observatory is good, return True
    return True

