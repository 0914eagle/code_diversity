
def count_good_observatories(elevations, roads):
    # Initialize a dictionary to store the elevations of each observatory and its neighbors
    observatories = {}
    for i in range(len(elevations)):
        observatories[i + 1] = {i + 1: elevations[i]}

    # Add the neighbors of each observatory and their elevations to the dictionary
    for road in roads:
        observatory1, observatory2 = road
        if observatory1 in observatories:
            observatories[observatory1][observatory2] = elevations[observatory2 - 1]
        else:
            observatories[observatory1] = {observatory2: elevations[observatory2 - 1]}

    # Count the number of good observatories
    count = 0
    for observatory, neighbors in observatories.items():
        max_elevation = max(neighbors.values())
        if elevations[observatory - 1] > max_elevation:
            count += 1

    return count

